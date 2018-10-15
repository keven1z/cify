#!/usr/bin/env python
# -*- coding:utf-8 -*-

######################################################### 
# (C) 2018 zii. All rights Reserved# 
#########################################################  
import threading


class Worker(threading.Thread):
    def __init__(self, system):
        threading.Thread.__init__(self)
        self.system = system

    def _run(self):
        raise Exception('unimplemented method')

    def run(self):
        self._run()

    def _do_job(self):
        raise Exception('unimplemented method')


class WorkerFactory(object):
    def __init__(self):
        pass

    @staticmethod
    def create_worker(cls, system):
        return cls(system)


if __name__ == '__main__':
    worker = WorkerFactory.create_worker(Worker, 's')
    worker.start()
