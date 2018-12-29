# __*__coding:utf-8__*__
# whois模块
#######################
# 检索url的域名信息
#######################

import sys
from common.plugin import Plugin
from common.log.log_util import LogUtil as log
import whois
from common.utils.printdata import *

logging = log.getLogger(__name__)


class CifyPlugin(Plugin):

    def __init__(self):
        super(CifyPlugin, self).__init__()
        self._id = 10001
        self.result = ResultExport.instance()

    def _run(self):
        hostname = self.wharehouse.wurl.hostname
        try:
            info('Starting whois ' + hostname)
            self.result.add_data('whois:')
            result = whois.whois(hostname)

            start_mark('RESULT WHOIS')
            result_print(result.text)
            self.result.add_data(result.text)
            end_mark()
            info('Whois done')
        except OSError as e:
            error('whois check failed')
            logging.error('whois check failed,reason:' + str(e))
            return


if __name__ == '__main__':
    from common.wharehouse import Wharehouse
    from common.net.webUtil import WrappedUrl

    w = Wharehouse()
    wurl = WrappedUrl('http://www.ghostz.com.cn')
    w.wurl = wurl
    CifyPlugin().run(w)
