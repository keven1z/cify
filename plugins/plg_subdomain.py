# __*__coding:utf-8__*__
# 子域名爆破模块
from common.log.logUtil import LogUtil as logging
from common.plugin import Plugin
from data.config import *
import os
import requests


logger = logging.getLogger(__name__)


class CifyPlugin(Plugin):
    def __init__(self):
        super(CifyPlugin, self).__init__()
        self._id = 10002
        self.ip = None
        self.subdomain_list = []
        self.alive_host = []
        self.count = 0

    def _run(self):
        cache_list = []
        wurl = self.wharehouse.wurl
        domain = wurl.domain
        schema = wurl.scheme
        for i in self._parse_dictionary():
            i = str(i, encoding='utf-8')
            i = schema + '://' + i + '.' + domain
            cache_list.append(i)
            if len(cache_list) > 10000:
                self.subdomain_list = cache_list
                self._process()
                cache_list.clear()

    def _parse_dictionary(self):
        try:
            with open(os.path.abspath(os.path.dirname(__file__)) + '/../' + SUBDOMAIN_DICTIONARY_PATH, 'rb') as f:

                line = f.readline()
                while line:
                    yield line.strip()
                    line = f.readline()
        except NotADirectoryError as e:
            logger.error(str(e))
        except FileNotFoundError as e:
            logger.error(str(e))

    def _is_alive(self, url):
        resp = requests.get(url, timeout=3)
        code = resp.status_code
        print(code)
        if 500 > code > 400:
            return
        else:
            self.alive_host.append(url)

    def _process(self):
        execute_by_thread(self._is_alive, self.subdomain_list)
        print(self.alive_host)


if __name__ == '__main__':
    from common.wharehouse import Wharehouse
    from common.net.webUtil import WrappedUrl

    w = Wharehouse()
    wurl = WrappedUrl('http://www.ghostz.com.cn')
    w.wurl = wurl
    CifyPlugin().run(w)
