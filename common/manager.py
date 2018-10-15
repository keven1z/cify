#########################################################
# (C)  zii .All rights Reserved#
#########################################################
import re
import os
from common.log.logUtil import LogUtil as logging

logger = logging.getLogger(__name__)


class Manager(object):
    def __init__(self):
        self.module_list = []
        self.module_hash = {}  # 以id为key，module为值存储

    def _load_module(self):
        raise Exception('unimplemented method')

    def load(self):
        self._load_module()
        logger.debug("load the spider==>%d", len(self.module_list))

    def _add_newest_module(self, modulelist, modulepath, pattern):
        # 选择最新的插件加载
        if os.path.exists(modulepath) and re.search(pattern, modulepath):
            filename, ext = os.path.splitext(modulepath)
            new_ext = ".py" if ext == ".pyc" else ".pyc"
            if (filename + new_ext) not in modulelist:
                modulelist.append(modulepath)
            else:
                if os.path.exists(filename + new_ext) and os.path.getmtime(modulepath) > os.path.getmtime(
                        filename + new_ext):
                    modulelist.remove(filename + new_ext)
                    modulelist.append(modulepath)
        return modulelist

    def get_modules(self):
        if len(self.module_list) == 0 and len(self.module_hash) == 0:
            self._load_module()
        return self.module_list, self.module_hash


class Module(object):
    def __init__(self):
        self.module_obj = None
        self.module_info = {}


class ModuleFactory(object):
    def __init__(self):
        pass

    @staticmethod
    def create_module():
        return Module()
