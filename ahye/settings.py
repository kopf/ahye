import os

DEBUG = True
VDIR = 's'
LOCAL_UPLOADS_DIR = os.path.join(os.path.abspath(os.path.curdir), 'ahye/static/uploads')
BASE_URL = 'http://192.168.92.80' # Used in documentation. Must NOT end in a slash.