import magic
import os
import random
import string

from ahye.settings import LOCAL_UPLOADS_DIR


def generate_filename(image_data, detect_extension=True):
    alphanum = string.ascii_letters + string.digits
    retval = ''
    while not retval or os.path.exists(os.path.join(LOCAL_UPLOADS_DIR, retval)): 
        retval = ''.join(random.sample(alphanum, 8))
        if detect_extension:
            retval += get_file_extension(image_data)
        else:
            retval += '.png'
    return retval

def get_file_extension(image_data):
    s = magic.from_buffer(image_data)
    if s.startswith('JPEG'):
        return '.jpg'
    elif s.startswith('GIF'):
        return '.gif'
    elif s.startswith('PNG'):
        return '.png'

def guess_file_extension(url):
    url = url.lower()
    if '.jpg' in url or '.jpeg' in url:
        return '.jpg'
    elif '.gif' in url:
        return '.gif'
    elif '.png' in url:
        return '.png'
    else:
        return '.jpg'
