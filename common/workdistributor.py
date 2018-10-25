#########################################################
# (C)  zii .All rights Reserved#
#########################################################

from common.worker import WorkerFactory
from worker.worker_port import PortWorker
from worker.work_whois import WhoisWorker
from common.wharehouse import Wharehouse


def work_port(wharehouse):
    if isinstance(wharehouse, Wharehouse):
        portworker = WorkerFactory.create_worker(PortWorker, wharehouse)
        portworker.start()
        whoisworker = WorkerFactory.create_worker(WhoisWorker, wharehouse)
        whoisworker.start()
