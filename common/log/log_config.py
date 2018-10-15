#!/usr/bin/env python
# -*- coding:utf-8 -*-

#########################################################
# (C)  zii .All rights Reserved#
#########################################################
import os
from cloghandler import ConcurrentRotatingFileHandler
from logging import handlers

log_file_backup_count = int(os.environ.get('LOG_FILE_BACKUP_COUNT', 10))
log_file_max_size = int(os.environ.get('LOG_FILE_MAX_SIZE', 128))
log_file_max_bytes = log_file_max_size << 20

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'verbose': {
            'format': '%(asctime)s %(levelname)s {%(process)d-%(thread)d %(module)s.%(funcName)s:%(lineno)d} %(message)s',
            'datefmt': '%y-%m-%d %H:%M:%S'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
        'result': {
            'format': '%(message)s'
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
        'debug': {
            'class': 'logging.handlers.ConcurrentRotatingFileHandler',
            'filename': os.path.realpath(__file__) + '/../../../log/' + 'debug.log',
            'maxBytes': log_file_max_bytes,
            'backupCount': log_file_backup_count,
            'debug': False,
            'formatter': 'verbose'
        },
        'result': {
            'class': 'logging.handlers.ConcurrentRotatingFileHandler',
            'filename': os.path.realpath(__file__) + '/../../../log/' + 'result.log',
            'maxBytes': log_file_max_bytes,
            'backupCount': log_file_backup_count,
            'debug': False,
            'formatter': 'result'
        },
        'socket': {
            'class': 'logging.handlers.SocketHandler',
            'host': '127.0.0.1',
            'port': int(os.environ.get('LOG_SERVER_PORT', handlers.DEFAULT_TCP_LOGGING_PORT)),
            'formatter': 'verbose'
        },
    },
    'loggers': {
        'socket': {
            'handlers': ['socket'],
            'level': 'NOTSET',
            'propagate': False,
        },
        'result': {
            'handlers': ['result'],
            'level': 'NOTSET',
            'propagate': False,
        },
    },
    'root': {
        'handlers': ['debug'],
        'level': 'NOTSET',
        'propagate': False,
    }
}
