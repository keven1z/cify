#!/usr/bin/env python
# -*- coding:utf-8 -*-

######################################################### 
# (C) 2000-2012 cseclabs Corporation. All rights Reserved# 
#########################################################  
# !/usr/bin/env python
# -*- coding:utf-8 -*-


import queue
import threading
import traceback
from data.config import *
from common.log.logUtil import LogUtil as logging

logger = logging.getLogger(__name__)


class ThreadPool(object):
    def __init__(self):
        self.task_queue = queue.Queue()
        self.threads = []
        self.__init_thread_pool(THREAD_NUMBER)

    def __init_thread_pool(self, thread_num):
        """
        the number of workers means the number of parallel running threads
        """
        for i in range(thread_num):
            worker = Worker(self.task_queue)
            worker.setDaemon(True)  # comment this line to avoid the main thread was end before subthread
            worker.start()

            self.threads.append(worker)
        # logger.debug('constructed a thread pool with %d workers', len(self.threads))

    def add_task(self, func, *args):
        """
        add a task to task queue
        """
        self.task_queue.put((func, args))

    def wait_all_complete(self):
        """
        this will block the thread until the task queue was empty
        """
        self.task_queue.join()
        self._terminate_workers()

    def force_complete(self):
        self.clear_tasks()
        self._terminate_workers()

    def clear_tasks(self):
        # logger.info('there are %d tasks in the queue that will be removed' % self.task_queue.qsize())
        while not self.task_queue.empty():
            self.task_queue.get_nowait()
            self.task_queue.task_done()
            # logger.debug('removed a task and %d remains' % self.task_queue.qsize())
        # logger.info('task queue was cleared and the size=%d' % self.task_queue.qsize())

    def _terminate_workers(self):
        # logger.debug('will terminate %d workers in thread pool', len(self.threads))
        for worker in self.threads:
            worker.terminate()


class Worker(threading.Thread):
    def __init__(self, task_queue):
        super(Worker, self).__init__()
        self.task_queue = task_queue
        self.stop = False

    def run(self):
        max_len = 64
        while not self.stop:
            try:
                do, args = self.task_queue.get(timeout=1)
                args_desc = str(args)
                if len(args_desc) > max_len:
                    args_desc = '%s...' % args_desc[0:max_len]
                #                logger.debug('get a task(function=%s, params=%s) and there are %d in queue' %
                #                             (do, args_desc, self.task_queue.qsize()))
                try:
                    do(*args)
                except:
                    logger.warn(traceback.format_exc())

                #                logger.debug('finish a task(function=%s, params=%s) and there are %d in queue' %
                #                             (do, args_desc, self.task_queue.qsize()))
                if self.stop:
                    #                    logger.info('the worker in thread pool was terminated')
                    pass

                self.task_queue.task_done()
            except:
                pass

    def terminate(self):
        self.stop = True
