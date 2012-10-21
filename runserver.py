#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Copyright 2011 Aengus Walton <ventolin@gmail.com>

from ahye import app
from ahye.settings import DEBUG
from ahye.flaskext.mako import init_mako

if __name__ == '__main__':
    app.config.update({
        'MAKO_DIR': 'ahye/templates',
        'MAKO_CACHEDIR': '/tmp',
        'MAKO_CACHESIZE': 500
    })
    init_mako(app)
    app.run(debug=DEBUG, host='0.0.0.0')
