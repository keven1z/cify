from common.worker import Worker
from plugins.pluginmanager import PluginManager
from spider.spidermanager import SpiderManager


class PortWorker(Worker):
    def __init__(self, system):
        super(PortWorker, self).__init__(system)
        self.system = system

    def _run(self):
        self._do_job()

    def _do_job(self):
        platform = self.system.platform
        if platform == 'linux' or platform == 'darwin':
            plghash = {}
            plglist = []
            plgManager = PluginManager()
            port_plugin_id = self.system.config.port_plugin_id
            if port_plugin_id is not None:
                plglist, plghash = plgManager.get_modules()
            plugins = plghash[port_plugin_id].module_obj
            plugins.run(self.system)
        else:
            spdManager = SpiderManager()
            spdhash={}
            spdlist=[]
            port_spider_id = self.system.config.port_spider_id
            if port_spider_id is not None:
                spdlist, spdhash = spdManager.get_modules()
            plugins = spdhash[port_spider_id].module_obj
            plugins.run(self.system)
