#!/usr/bin/env python
# -*- coding:utf-8 -*-
###########################
# 插件类                   #
###########################
from common.log.logUtil import LogUtil


class Plugin(object):

    def __init__(self):
        self._id = -1
        self.system = None

    @property
    def id(self):
        return self._id

    def run(self, system):
        self.system = system
        self._run()

    def _run(self):
        raise Exception('unimplemented method')
