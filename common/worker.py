#!/usr/bin/env python
# -*- coding:utf-8 -*-

######################################################### 
# (C) 2018 zii. All rights Reserved# 
#########################################################  
import threading
import time


class Worker(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self) 
		self.param = None

	def _run(self):
		raise Exception('unimplemented method')

	def run(self):
		self._run()

	def set_job(self, param):
		self.param = param

	def do_job(self, job):
		raise Exception('unimplemented method')


