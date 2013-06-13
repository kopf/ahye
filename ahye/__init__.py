# -*- coding: utf-8 -*-

#Copyright 2011 Aengus Walton <ventolin@gmail.com>

from flask import Flask

__author__ = 'Aengus Walton'
__version__ = '0.2'
__homepage__ = 'https://github.com/kopf/ahye-server'

app = Flask(__name__)

from . import views
