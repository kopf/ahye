import os
import json
import uuid

from flask import (abort, redirect, request, jsonify,
                   send_from_directory, url_for)
import requests

from ahye import app
from ahye.flaskext.mako import render_template as render
from ahye.lib import generate_filename
from ahye.settings import VDIR, LOCAL_UPLOADS_DIR


@app.route('/', methods=['GET'])
def home():
    return render('/home.mako')


@app.route('/upload', methods=['POST'])
def upload():
    data = request.files['imagedata']
    filename = generate_filename()
    data.save(os.path.join(LOCAL_UPLOADS_DIR, filename))
    return url_for('serve_upload', filename=filename, _external=True)


@app.route('/webupload', methods=['POST'])
def webupload():
    retval = []
    for newimg in request.files.getlist('files[]'):
        filename = generate_filename()
        newimg.save(os.path.join(LOCAL_UPLOADS_DIR, filename))
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
    if not url.endswith(('.jpg', '.png', '.jpeg', '.gif')):
        abort(400)
    filename = uuid.uuid3(uuid.NAMESPACE_DNS, url) + '.png'
    if not os.path.exists(os.path.join(LOCAL_UPLOADS_DIR, filename)):
        conn = requests.get(url)
        if 200 <= conn.status_code <= 300:
            with open(os.path.join(LOCAL_UPLOADS_DIR, filename), 'w') as f:
                f.write(conn.content)
        else:
            abort(conn.status_code)
    return redirect(url_for('serve_upload', filename=filename, _external=True))


@app.route('/favicon.ico')
def serve_favicon():
    return send_from_directory(os.path.join(LOCAL_UPLOADS_DIR, '..'), 'favicon.ico')
