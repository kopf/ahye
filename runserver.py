#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Copyright 2011 Aengus Walton <ventolin@gmail.com>

from ahye import app
from ahye.settings import DEBUG

if __name__ == '__main__':
    app.run(debug=DEBUG, host='0.0.0.0')
