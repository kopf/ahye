import os

from flask import request, send_from_directory

from ahye.settings import SERVER, LOCAL_UPLOADS_DIR
from ahye.lib import get_filename
from ahye import app

@app.route('/upload', methods=['POST'])
def upload():
    data = request.files['imagedata']
    filename = get_filename()
    data.save(os.path.join(LOCAL_UPLOADS_DIR, filename))

    return 'http://%s:%s/%s/%s' % (SERVER['host'], SERVER['port'],
                                   SERVER['dir'], filename)

@app.route('/%s/<filename>' % SERVER['dir'])
def serve_upload(filename):
    return send_from_directory(LOCAL_UPLOADS_DIR, filename)

