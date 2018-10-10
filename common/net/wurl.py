# __*__coding:utf-8__*__
from urllib.parse import urlparse
from common.net.constant import HttpConstant
from common.log.logUtil import LogUtil as logging

logging = logging.instance().getLogger()


class Wurl(object):
    """docstring for Wurl"""

    def __init__(self, url, **kwargs):
        self._request = WrappedRequest(**kwargs)
        self._url = url

    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, url):
        self._url = url

    @property
    def port(self):
        components = urlparse(self._url)
        port = components.port
        if port is None:
            if components.scheme == 'http':
                port = 80
            elif components.scheme == 'https':
                port = 443
        return port

    @property
    def hostname(self):
        components = urlparse(self._url)
        hostname = components.hostname
        return hostname

    @property
    def method(self):
        return self._request.method

    @method.setter
    def method(self, method):
        self._request.method = method

    @property
    def req_headers(self):
        return self._request.headers

    @req_headers.setter
    def req_headers(self, headers):
        self._request.headers = headers

    @property
    def post_data(self):
        return self._request.post_data

    @post_data.setter
    def post_data(self, data):
        self._request.post_data = data

    @property
    def proxy(self):
        return self._request.proxy

    @proxy.setter
    def proxy(self, proxy):
        self._request.proxy = proxy

    @property
    def auth(self):
        return self._request.auth

    @auth.setter
    def auth(self, auth):
        self._request.auth = auth

    @property
    def cert(self):
        return self._request.cert

    @cert.setter
    def cert(self, cert):
        self._request.cert = cert

    @property
    def cookies(self):
        return self._request.cookies


class WrappedRequest(object):
    def __init__(self, method=HttpConstant.GET, headers={}, proxy=None, auth=None, cookies=None, \
                 data='', timeout=None, allow_redirects=False, desc_text="", **kwargs):
        kwargs = dict(kwargs)
        kwargs['method'] = method
        kwargs['allow_redirects'] = allow_redirects
        kwargs['headers'] = dict(headers)
        if proxy:
            kwargs['proxy'] = proxy
        if auth:
            kwargs['auth'] = auth

        if data:
            kwargs['data'] = data
        if timeout:
            kwargs['timeout'] = timeout

        kwargs['text'] = desc_text

        self._kwargs = kwargs

    @property
    def method(self):
        return self._kwargs.get('method')

    @method.setter
    def method(self, method):
        self._kwargs['method'] = method

    @property
    def headers(self):
        return self._kwargs.get('headers')

    @headers.setter
    def headers(self, headers):
        self._kwargs['headers'] = headers

    @property
    def proxy(self):
        return self._kwargs.get('proxy')

    @proxy.setter
    def proxy(self, proxy):
        self._kwargs['proxy'] = proxy

    @property
    def auth(self):
        return self._kwargs.get('auth')

    @auth.setter
    def auth(self, auth):
        self._kwargs['auth'] = auth

    @property
    def cert(self):
        return self._kwargs.get('cert')

    @cert.setter
    def cert(self, cert):
        self._kwargs['cert'] = cert

    @property
    def cookies(self):
        return self._kwargs.get('cookies')

    @cookies.setter
    def cookies(self, cookies):
        self._kwargs['cookies'] = cookies

    @property
    def post_data(self):
        return self._kwargs.get('data')

    @post_data.setter
    def post_data(self, data):
        self._kwargs['data'] = data

    @property
    def text(self):
        return self._kwargs.get('text')

    @text.setter
    def text(self, text):
        self._kwargs['text'] = text

    @property
    def kwargs(self):
        return self._kwargs

    def __str__(self):
        return '<%s %s>' % (self.__class__, self.method)

if __name__ == '__main__':
    wurl=Wurl('http://www.baidu.com')
    print(wurl.hostname)