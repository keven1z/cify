##################################
# 爬虫管理（包含）#
##################################
from common.log.log_util import LogUtil as log
import sys
import os
import traceback
import importlib.util
from common.manager import *

logger = log.getLogger(__name__)


class PluginManager(Manager):
    def __init__(self):
        super(PluginManager, self).__init__()
        pass

    def _load_module(self):
        spd_home = os.path.dirname(os.path.abspath(__file__))
        results = []
        for root, plugin_dirs, files in os.walk(spd_home):
            for name in files:
                results = self._add_newest_module(results, os.path.join(root, name), r'plg.*\.py?$')
        for result in results:
            path = os.path.dirname(result)
            if path not in sys.path:
                sys.path.append(path)
            filename, ext = os.path.splitext(result)
            try:
                mod_name = filename.replace('/', '|')
                module_spec = importlib.util.spec_from_file_location(mod_name, result)
                module = importlib.util.module_from_spec(module_spec)
                module_spec.loader.exec_module(module)
            except Exception as e:
                logger.error(traceback.format_exc())
                continue
            container = ModuleFactory.create_module()
            if hasattr(module, "CifyPlugin"):
                obj = module.CifyPlugin()
                container.module_obj = obj
                container.module_info['id'] = obj._id
            if container.module_obj is not None:
                self.module_list.append(container)
                id = str(container.module_info['id'])
                self.module_hash[id] = container


if __name__ == '__main__':
    sm = PluginManager()
    sm.load()
    print(sm.module_hash['10000'].module_obj)
