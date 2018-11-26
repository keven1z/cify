# -*- coding:utf-8 -*-

from common.log.logUtil import LogUtil as logging

import requests
from common.net.url import WrappedUrl, WrappedResponse
import time
import requests_cache

from common.net.constant import HttpConstant

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
        wresp = self.do_request(wurl, **kwargs)
        return wresp

    def do_request(self, wurl, **kwargs):
        start_time = time.time()
        w_resp = None
        try:
            resp = self.client.request(wurl.method, wurl.url, **kwargs)
            w_resp = self._wrap_resp(resp, encoding=None)
        except requests.exceptions.ConnectionError:
            logger.info('ConnectionError when access %s', wurl.url)
            w_resp = WrappedResponse(status_code=HttpConstant.RC_ERROR, error_code=0)
        except requests.exceptions.ChunkedEncodingError:
            logger.error('ChunkedEncodingError when access %s', wurl.url)
            w_resp = WrappedResponse(status_code=HttpConstant.RC_ERROR)
        except requests.exceptions.Timeout:
            logger.error('Timeout when access %s', wurl.url)
            w_resp = WrappedResponse(status_code=HttpConstant.RC_ERROR)
        except Exception as e:
            logger.error('Timeout when access %s', wurl.url)
            w_resp = WrappedResponse(status_code=HttpConstant.RC_ERROR)
        finally:
            if w_resp is not None:
                used_time = time.time() - start_time
                logger.info("totally used %s to request %s, response %s", used_time, wurl.url, w_resp.status_code)
            return w_resp

    def _wrap_resp(self, resp, encoding=None):

        return WrappedResponse(status_code=resp.status_code, headers=resp.headers, \
                               content=resp.content, cookies=resp.cookies, history=resp.history, \
                               encoding=encoding, raw_headers=resp.headers, total_time=None, reason=resp.reason)


if __name__ == '__main__':
    web = Request()
    res = web.request(WrappedUrl("http://www.baidu.com"))
    print(res)
