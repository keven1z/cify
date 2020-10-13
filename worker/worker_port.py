from common.worker import Worker
from plugins.pluginmanager import PluginManager


class PortWorker(Worker):
    def __init__(self, wharehouse):
        super(PortWorker, self).__init__(wharehouse)
        self.wharehouse = wharehouse

    def _run(self):
        self._do_job()

    def _do_job(self):
        platform = self.wharehouse.platform
        if platform == 'linux' or platform == 'darwin':
            plghash = {}
            plgManager = PluginManager()
            port_plugin_id = self.wharehouse.config.port_plugin_id
            if port_plugin_id is not None:
                plglist, plghash = plgManager.get_modules()
            plugins = plghash[port_plugin_id].module_obj
            plugins.run(self.wharehouse)
            import data.data as data
            data.RESULT.update({'port': plugins.result})
