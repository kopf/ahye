import string
import random
import os

from ahye.settings import LOCAL_UPLOADS_DIR

def get_filename():
    alphanum = string.ascii_letters + string.digits

    def generate_filename():
        filename = ''
        for i in range(0,8):
            filename += random.choice(alphanum)
        return filename + '.png'

    retval = ''
    
    while not retval or os.path.exists(os.path.join(LOCAL_UPLOADS_DIR, retval)): 
        retval = generate_filename() 
    return retval

