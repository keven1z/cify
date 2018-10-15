#!/usr/bin/env python
# -*- coding:utf-8 -*-

#########################################################
# (C)  zii .All rights Reserved#
#########################################################

#########################################################
# (C) 日志打印工具#
#########################################################

import threading
from common.log import log_config


class LogUtil(object):
    import logging
    from logging import config
    config.dictConfig(log_config.LOGGING)
    _mutex = threading.Condition()

    ERROR = logging.ERROR
    WARN = logging.WARN
    INFO = logging.INFO
    DEBUG = logging.DEBUG

    @staticmethod
    def getLogger(name=None, via_socket=True):
        if name and name.find("result") != -1:
            name = 'result'
        import logging
        logger = logging.getLogger(name)

        return logger


if __name__ == '__main__':
    logger = LogUtil.getLogger('debug')
    logger.debug('text')
