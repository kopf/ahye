import hashlib
import os
import json
import urlparse

from flask import (abort, redirect, request, send_from_directory, url_for,
                   render_template as render)
import requests

from ahye import app
from ahye.lib import generate_filename, guess_file_extension
from ahye.settings import VDIR, LOCAL_UPLOADS_DIR, BASE_URL


@app.route('/', methods=['GET'])
def home():
    return render('/home.html', base_url=BASE_URL.strip('/'))


@app.route('/upload', methods=['POST'])
def upload():
    data = request.files['imagedata']
    filename = generate_filename(data, detect_extension=False)
    data.save(os.path.join(LOCAL_UPLOADS_DIR, filename))
    return url_for('serve_upload', filename=filename, _external=True)


@app.route('/webupload', methods=['POST'])
def webupload():
    retval = []
    for newimg in request.files.getlist('files[]'):
        data = newimg.stream.read()
        filename = generate_filename(data)
        with open(os.path.join(LOCAL_UPLOADS_DIR, filename), 'w') as f:
            f.write(data)
        retval.append({
            "name":filename,
            "size":0,
            "url":"/{0}/{1}".format(VDIR, filename),
            "thumbnail_url":"/blah.jpg",
            "delete_url":"/blah",
            "delete_type":"DELETE"
        })
    return json.dumps(retval)


@app.route('/%s/<filename>' % VDIR)
def serve_upload(filename):
    return send_from_directory(LOCAL_UPLOADS_DIR, filename)


@app.route('/<path:url>')
def crossload(url):
    if not url.startswith('http:/') and not url.startswith('https:/'):
        abort(404)

    # reconstruct url (query string has been stripped from url by flask)
    if request.query_string:
        url = '%s?%s' % (url, request.query_string)

    # rewrite url as apache's mod_rewrite converts // to /
    if url.startswith('http:/') and not url.startswith('http://'):
        url = url.replace('http:/', 'http://')
    elif url.startswith('https:/') and not url.startswith('https://'):
        url = url.replace('https:/', 'https://')

    filename = '%s%s' % (hashlib.md5(url.encode('utf-8')).hexdigest(),
                         guess_file_extension(url))

    parsed_url = urlparse.urlparse(url)
    auth = (parsed_url.username, parsed_url.password)

    if not os.path.exists(os.path.join(LOCAL_UPLOADS_DIR, filename)):
        try:
            conn = requests.get(url, auth=auth, verify=False)
        except requests.exceptions.ConnectionError:
            return render('/error.html',
                          error={'msgs': ['Connection to server failed.',
                                          'Is it a valid domain?']})
        except (requests.exceptions.InvalidSchema,
                requests.exceptions.MissingSchema,
                requests.exceptions.InvalidURL):
            return render('/error.html',
                          error={'msgs': ['Invalid URL.',
                                          'Please check and try again.']})
        except requests.exceptions.Timeout:
            return render('/error.html',
                          error={'msgs': ['Connection to server timed out.']})
        except Exception:
            return render('/error.html')

        if 200 <= conn.status_code <= 300:
            with open(os.path.join(LOCAL_UPLOADS_DIR, filename), 'w') as f:
                f.write(conn.content)
        else:
            return render('/error.html', error={'code': conn.status_code})
    return redirect(url_for('serve_upload', filename=filename, _external=True))


@app.route('/favicon.ico')
def serve_favicon():
    return redirect(url_for('static', filename='favicon.ico'))


@app.route('/robots.txt')
def serve_robots():
    return redirect(url_for('static', filename='robots.txt'))
