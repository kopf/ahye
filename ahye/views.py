import os

from flask import (abort, redirect, request,
                   send_from_directory, url_for)
import requests

from ahye.settings import VDIR, LOCAL_UPLOADS_DIR
from ahye.lib import generate_filename
from ahye import app

@app.route('/upload', methods=['POST'])
def upload():
    data = request.files['imagedata']
    filename = generate_filename()
    data.save(os.path.join(LOCAL_UPLOADS_DIR, filename))
    return url_for('serve_upload', filename=filename, _external=True)


@app.route('/%s/<filename>' % VDIR)
def serve_upload(filename):
    return send_from_directory(LOCAL_UPLOADS_DIR, filename)

@app.route('/<path:url>')
def crossload(url):
    if not url.endswith(('.jpg', '.png', '.jpeg', '.gif')):
        abort(400)
    conn = requests.get(url)
    if 200 <= conn.status_code <= 300:
        filename = generate_filename()
        with open(os.path.join(LOCAL_UPLOADS_DIR, filename), 'w') as f:
            f.write(conn.content)
        return redirect(url_for('serve_upload', filename=filename, _external=True))
    else:
        abort(conn.status_code)


@app.route('/favicon.ico')
def serve_favicon():
    return send_from_directory(os.path.join(LOCAL_UPLOADS_DIR, '..'), 'favicon.ico')
