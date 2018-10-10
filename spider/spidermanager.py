##################################
# 爬虫管理（包含）#
##################################
from common.log.logUtil import LogUtil as logging
import sys
import os
import traceback
import importlib.util
from common.manager import *

logger = logging.instance().getLogger()


class SpiderManager(Manager):
    def __init__(self):
        super(SpiderManager, self).__init__()
        pass

    def _load_module(self):
        spd_home = os.path.dirname(os.path.abspath(__file__))
        results = []
        for root, plugin_dirs, files in os.walk(spd_home):
            for name in files:
                results = self._add_newest_module(results, os.path.join(root, name), r'\\spd.*\.py?$')
        for result in results:
            path = os.path.dirname(result)
            if path not in sys.path:
                sys.path.append(path)
            filename, ext = os.path.splitext(result)
            try:
                mod_name = filename.replace('/', '|')
                module_spec = importlib.util.spec_from_file_location(mod_name, result)
                spdmodule = importlib.util.module_from_spec(module_spec)
                module_spec.loader.exec_module(spdmodule)
            except Exception as e:
                logger.error(traceback.format_exc())
                continue
            container = ModuleFactory.create_module()
            if hasattr(spdmodule, "CifySpider"):
                spdobj = spdmodule.CifySpider()
                container.module_obj = spdobj
                container.module_info['id'] = spdobj.s_id
            if container.module_obj is not None:
                self.module_list.append(container)
                _id=str(container.module_info['id'])
                self.module_hash[_id] = container


if __name__ == '__main__':
    sm = SpiderManager()
    sm.load()
    print(sm.module_hash['10000'].module_obj)
