#!/usr/bin/python
import logging
from logging import config
from logging import getLogger
import os

def create_log_file(file_name='example_log.txt'):
    if not os.path.isdir('log'):
        os.mkdir('log')
    if not os.path.isfile(os.path.join('log',file_name)):
        open(os.path.join('log', file_name), 'a').close()

def write_log_without_setting_file():
    FORMAT = r'%(asctime)-15s [%(levelname)s] : %(message)s'
    #FORMAT = r'%(asctime)-15s [%(levelno)s] : %(message)s'
    logging.basicConfig(filename=file_name, format=FORMAT, level=logging.DEBUG)
    #Write log
    logging.debug('This is a debug level log.')
    logging.info('This is a info log, if you set level to warning, you will not see this log.')
    logging.warning('This is a warning, if you set level to error, you will not see this log')
    logging.error('This is a error, if you set level to critical, you will not see this log')
    logging.critical('This is a critical.')

def write_log_with_setting_file():
    config.fileConfig('./logging.cnf')
    logger = getLogger(__file__)

    logger.debug('Debug message.')
    logger.info('Infor message.')
    logger.warn('Warning message.')
    logger.error('Error message.')
    logger.critical('Critical message.')

if __name__ == '__main__':
    write_log_with_setting_file()
