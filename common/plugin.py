#!/usr/bin/env python
# -*- coding:utf-8 -*-
###########################
#插件类                   #
###########################
from common.log.logUtil import LogUtil

class Plugin( object ):

    def __init__(self):
        self._id=-1

    @property
    def id(self):
        return self._id

    def _run(self, wurl):
        raise Exception('unimplemented method')

    def cmd_run(self, wurl):
        self._run(wurl)
