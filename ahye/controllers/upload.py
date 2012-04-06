import logging
import random
import os

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from ahye.lib.base import BaseController, render
import ahye.lib.helpers as h

log = logging.getLogger(__name__)

class UploadController(BaseController):
    
    uploads_dir = os.path.join('ahye', 'public', 'uploads')

    def main(self):
        data = request.POST['imagedata'].value
        filename = self._get_filename()
        success = self._save_image(data, filename)
        if success:
            return 'http://192.168.92.80/uploads/%s' % filename 
        else:
            log.error("Failed to save, returning 501")
            # TODO

    def _save_image(self, data, filename):
        log.debug("Saving to %s" % filename)
        try:
            f = open(os.path.join(self.uploads_dir, filename), 'wb')
            f.write(data)
            f.close()
        except Exception:
            return False
        return True

    def _get_filename(self):
        alphanum = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'

        def generate_filename():
            filename = ''
            for i in range(0,8):
                filename += random.choice(alphanum)
            return filename + '.png'

        retval = ''
        while not retval or os.path.exists(os.path.join(self.uploads_dir, retval)):
            retval = generate_filename() 
        return retval
         
