from common.manager import *
from common.log.logUtil import LogUtil as logging
import sys
import os
import traceback
import importlib.util

logger = logging.instance().getLogger()


class RulerManager(Manager):
    def __init__(self):
        super(RulerManager, self).__init__()

    def _load_module(self):
        module_home = os.path.dirname(os.path.abspath(__file__))
        results = []
        for root, plugin_dirs, files in os.walk(module_home):
            for name in files:
                results = self._add_newest_module(results, os.path.join(root, name), r'ruler.*\.py?$')
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
            if hasattr(module, "CifyRuler"):
                module = module.CifyRuler()
                container.module_obj = module
                container.module_info['id'] = module.ruler_id
            if container.module_obj is not None:
                self.module_list.append(container)
                _id = container.module_info['id']
                if isinstance(_id, int):
                    _id = str(_id)
                self.module_hash[_id] = container


if __name__ == '__main__':
    rm = RulerManager()
    rm.load()
    list, hash = rm.get_modules()
    print(list, hash)
