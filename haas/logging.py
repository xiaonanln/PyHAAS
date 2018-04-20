import logging

logging.basicConfig(level=logging.DEBUG,
                    format='levelname:%(levelname)s filename: %(filename)s '
                           'outputNumber: [%(lineno)d]  thread: %(threadName)s output msg:  %(message)s'
                           ' - %(asctime)s', datefmt='[%d/%b/%Y %H:%M:%S]')
debug = logging.debug
info = logging.info
error = logging.error
warning = logging.warning


