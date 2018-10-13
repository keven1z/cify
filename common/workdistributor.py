###############
# 工作分配######
###############
from common.worker import WorkerFactory
from worker.worker_port import PortWorker
from common.systeminfo import System


def work_port(system):
    if isinstance(system, System):
        portworker = WorkerFactory.create_worker(PortWorker, system)
        portworker.start()
