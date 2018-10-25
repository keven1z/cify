from common.worker import Worker
from plugins.pluginmanager import PluginManager
from spider.spidermanager import SpiderManager


class WhoisWorker(Worker):
    def __init__(self, wharehouse):
        super(WhoisWorker, self).__init__(wharehouse)
        self.wharehouse = wharehouse

    def _run(self):
        self._do_job()

    def _do_job(self):
        platform = self.wharehouse.platform
        if platform == 'linux' or platform == 'darwin':
            plghash = {}
            plglist = []
            plgManager = PluginManager()
            whois_plugin_id = self.wharehouse.config.whois_plugin_id
            if whois_plugin_id is not None:
                plglist, plghash = plgManager.get_modules()
            plugins = plghash[whois_plugin_id].module_obj
            plugins.run(self.wharehouse)
        else:
            spdManager = SpiderManager()
            spdhash={}
            spdlist=[]
            port_spider_id = self.system.config.whois_plugin_id
            if port_spider_id is not None:
                spdlist, spdhash = spdManager.get_modules()
            plugins = spdhash[whois_plugin_id].module_obj
            plugins.run(self.wharehouse)