# -*- coding: utf-8 -*-

#Copyright 2011 Aengus Walton <aengus.walton@edelight.de>

from flask import Flask

__author__ = 'Aengus Walton'
__version__ = '0.2'
__homepage__ = 'https://github.com/edelight/ahye-server'

app = Flask(__name__)

import views
