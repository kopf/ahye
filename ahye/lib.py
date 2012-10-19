import string
import random
import os

from ahye.settings import LOCAL_UPLOADS_DIR

def generate_filename():
    alphanum = string.ascii_letters + string.digits
    retval = ''
    while not retval or os.path.exists(os.path.join(LOCAL_UPLOADS_DIR, retval)): 
        retval = ''.join(random.sample(alphanum, 8)) + '.png'
    return retval
