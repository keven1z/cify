# -*- coding:utf-8 -*-

from common.log.logUtil import LogUtil as logging
from common.net.constant import HttpConstant
import requests
import traceback
import time
import requests_cache

logger = logging.instance().getLogger()


class Web():
    def __init__(self):
        self.client = requests
        pass

    def request(self, method=HttpConstant.GET, url=None, iscache=False, **kwargs):
        if url is not None:
            resp = self.do_request(method, url, iscache, **kwargs)
            return resp
        else:
            logger.error('Url is None')
            return None

    def do_request(self, method, url, iscache=False, **kwargs):
        start_time = time.time()
        resp = None
        try:
            if iscache:
                requests_cache.install_cache('proxy_cache', backend='sqlite', expire_after=180)
            resp = self.client.request(method, url, **kwargs)
        except requests.exceptions.ConnectionError:
            logger.info('ConnectionError when access %s', url)
        except requests.exceptions.ChunkedEncodingError:
            logger.error('ChunkedEncodingError when access %s', url)
        except requests.exceptions.Timeout:
            logger.error('Timeout when access %s', url)
        except Exception as e:
            logger.error('Timeout when access %s', url)
        finally:
            if resp:
                used_time = time.time() - start_time
                logger.info("totally used %s to request %s, response %s", used_time, url, resp.status_code)
            return resp


if __name__ == '__main__':
    web = Web()
    res = web.request("GET", "http://www.baidu.com")
