"""Setup the ahye application"""
import logging

from ahye.config.environment import load_environment

log = logging.getLogger(__name__)

def setup_app(command, conf, vars):
    """Place any commands to setup ahye here"""
    # Don't reload the app if it was loaded under the testing environment
    load_environment(conf.global_conf, conf.local_conf)
