#!/usr/bin/env python
# -*- coding:utf-8 -*-

######################################################### 
# (C) 2018 zii. All rights Reserved# 
#########################################################  
import threading
import time


class Worker(threading.Thread):
    def __init__(self, wurl):
        threading.Thread.__init__(self)
        self.wurl = wurl

    def _run(self):
        raise Exception('unimplemented method')

    def run(self):
        self._run()

    def _do_job(self):
        raise Exception('unimplemented method')
