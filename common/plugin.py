#!/usr/bin/env python
# -*- coding:utf-8 -*-
#########################################################
# (C)  zii .All rights Reserved#
#########################################################

###########################
# 插件类                   #
###########################



class Plugin(object):

    def __init__(self):
        self._id = -1
        self.wharehouse = None

    @property
    def id(self):
        return self._id

    def run(self, wharehouse):
        self.wharehouse = wharehouse
        self._run()

    def _run(self):
        raise Exception('unimplemented method')
