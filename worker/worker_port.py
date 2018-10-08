from common.worker import Worker
from plugins.pluginmanager import PluginManager


class PortWorker(Worker):
    def __init__(self, wurl):
        super(PortWorker, self).__init__(wurl)

    def _run(self):
        self._do_job()

    def _do_job(self):
        plgManager = PluginManager()


class WorkerFactory(object):
    def __init__(self):
        pass

    @staticmethod
    def create_worker():
        return Worker()
