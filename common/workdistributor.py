#########################################################
# (C)  zii .All rights Reserved#
#########################################################

from common.worker import WorkerFactory
from worker.worker_port import PortWorker
from common.wharehouse import Wharehouse


def work_port(wharehouse):
    if isinstance(wharehouse, Wharehouse):
        portworker = WorkerFactory.create_worker(PortWorker, wharehouse)
        portworker.start()
