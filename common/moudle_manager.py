# -*- coding:utf-8 -*-
from common.worker import WorkerFactory
from worker.worker_port import PortWorker
from worker.work_whois import WhoisWorker
from worker.work_cms import CmsWorker
from common.utils.printdata import *
import sys


class MoudleManager(object):

    def __init__(self, ):
        pass

    def load_moudle(self, wharehouse):
        self._load_cms_moudle(wharehouse)
        self._load_port_moudle(wharehouse)
        self._load_whois_moudle(wharehouse)

    def _load_cms_moudle(self, wharehouse):
        cms_worker = WorkerFactory.create_worker(CmsWorker, wharehouse)
        cms_worker.start()
        cms_worker.join()

    def _load_port_moudle(self, wharehouse):
        port_worker = WorkerFactory.create_worker(PortWorker, wharehouse)
        try:
            port_worker.start()
            port_worker.join()
        except KeyboardInterrupt:
            warn('System has been exited')
            sys.exit(1)

    def _load_whois_moudle(self, wharehouse):
        whois_worker = WorkerFactory.create_worker(WhoisWorker, wharehouse)
        whois_worker.start()
        whois_worker.join()
