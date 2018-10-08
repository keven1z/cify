# __*__coding:utf-8__*__
# whois模块
#######################
# 检索url的域名信息
#######################

import sys
from common.plugin import Plugin
from common.log.logUtil import LogUtil as logging

logging = logging.instance().getLogger()


class CifyPlugin(Plugin):

    def __init__(self):
        super(CifyPlugin, self).__init__()
        self._id = 10001

    def _run(self):
        platform = sys.platform  # 获取操作系统信息
        if platform == 'win32':  # windows系统
            pass
        elif platform == 'linux':  # Linux系统
            pass
