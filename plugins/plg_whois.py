# __*__coding:utf-8__*__
# whois模块
#######################
# 检索url的域名信息
#######################

import sys
from common.plugin import Plugin
import whois
import data.data as data
from common.utils.printdata import *

logging = log.getLogger(__name__)
import datetime


class CifyPlugin(Plugin):

    def __init__(self):
        super(CifyPlugin, self).__init__()
        self._id = 10001

    def _run(self):
        info("Start whois")
        hostname = self.wharehouse.wurl.hostname
        try:
            result = whois.whois(hostname)
            for k, v in result.items():
                if isinstance(v, datetime.datetime):
                    v = str(v)
                    result.update({k: v})
            self.result = result
        except OSError as e:
            error('whois check failed')
            logging.error('whois check failed,reason:' + str(e))
            return
