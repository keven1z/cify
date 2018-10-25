# __*__coding:utf-8__*__
# whois模块
#######################
# 检索url的域名信息
#######################

import sys
from common.plugin import Plugin
from common.log.logUtil import LogUtil as logging
import whois
from common.utils.print import *

logging = logging.getLogger(__name__)


class CifyPlugin(Plugin):

    def __init__(self):
        super(CifyPlugin, self).__init__()
        self._id = 10001

    def _run(self):
        hostname = self.wharehouse.wurl.hostname
        result = whois.whois(hostname)
        info('Starting whois')
        start_mark('RESULT WHOIS')
        result_print(result.text)
        end_mark()
        info('Whois done')


if __name__ == '__main__':
    from common.wharehouse import Wharehouse
    from common.net.webUtil import WrappedUrl

    w = Wharehouse()
    wurl = WrappedUrl('http://www.ghostz.com.cn')
    w.wurl = wurl
    CifyPlugin().run(w)
