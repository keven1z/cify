# -*- coding:utf-8 -*-

from common.log.logUtil import LogUtil as logging

import requests
from common.net.url import WrappedUrl
import time
import requests_cache

#########################################################
# (C)  zii .All rights Reserved#
#########################################################
logger = logging.getLogger(__name__)


class Request(object):
    def __init__(self):
        self.client = requests
        pass

    def request(self, wurl, **kwargs):
        if not isinstance(wurl, WrappedUrl):
            logger.error('wurl is not WrappedUrl')
            raise Exception
        resp = self.do_request(wurl, **kwargs)
        return resp

    def do_request(self, wurl, **kwargs):

        start_time = time.time()
        resp = None
        try:
            if wurl.allow_cache:
                requests_cache.install_cache('cache', backend='sqlite', expire_after=180)
            resp = self.client.request(wurl.method, wurl.url, **kwargs)
        except requests.exceptions.ConnectionError:
            logger.info('ConnectionError when access %s', wurl.url)
        except requests.exceptions.ChunkedEncodingError:
            logger.error('ChunkedEncodingError when access %s', wurl.url)
        except requests.exceptions.Timeout:
            logger.error('Timeout when access %s', wurl.url)
        except Exception as e:
            logger.error('Timeout when access %s', wurl.url)
        finally:
            if resp:
                used_time = time.time() - start_time
                logger.info("totally used %s to request %s, response %s", used_time, wurl.url, resp.status_code)
            return resp


if __name__ == '__main__':
    web = Request()
    res = web.request(WrappedUrl("http://www.baidu.com"))
