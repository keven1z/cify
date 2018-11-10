# __*__coding:utf-8__*__
from urllib.parse import urlparse
from common.net.constant import HttpConstant
from common.log.logUtil import LogUtil as logging
from tld import get_fld
import lxml.html
import traceback
import re

#########################################################
# (C)  zii .All rights Reserved#
#########################################################


logger = logging.getLogger(__name__)


class WrappedUrl(object):
    """docstring for WrappedUrl"""

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
    def domain(self):
        domain = get_fld(self._url)
        return domain

    @property
    def scheme(self):
        components = urlparse(self._url)
        scheme = components.scheme
        return scheme

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

    @property
    def allow_cache(self):
        return self._request.allow_cache


class WrappedRequest(object):
    def __init__(self, method=HttpConstant.GET, allow_cache=False, headers={}, proxy=None, auth=None, cookies=None, \
                 data='', timeout=None, allow_redirects=False, desc_text="", **kwargs):
        kwargs = dict(kwargs)
        kwargs['method'] = method
        kwargs['allow_cache'] = allow_cache
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
    def allow_cache(self):
        return self._kwargs.get('allow_cache')

    @allow_cache.setter
    def allow_cache(self, allow_cache):
        self._kwargs['allow_cache'] = allow_cache

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


def _is_text_response(headers):
    if headers.has_key('Content-Type'):
        is_text = headers['Content-Type'].lower().find('text') > -1
        return is_text
    else:
        return True


def is_valid_encoding(encoding):
    try:
        import codecs
        codecs.lookup(encoding)
        return True
    except Exception:
        return False


def _get_encoding(headers, content):
    encoding = _get_encoding_from_header(headers)
    if not encoding or not is_valid_encoding(encoding):
        encoding = _get_encoding_from_content(content)
    if (not encoding or not is_valid_encoding(encoding)) and content:
        encoding = 'utf-8'
    # logger.debug('get charset=%s for the response content', encoding)
    return encoding


def _get_encoding_from_header(headers):
    encoding = None
    if 'Content-Type' in headers.keys():
        results = re.findall(r'charset=([a-z0-9-_]*)', headers['Content-Type'].lower())
        if len(results) == 1:
            encoding = results[0].lower()
    return encoding


def _get_encoding_from_content(html):
    if not html:
        return
    charset = None
    html = str(html, encoding="utf-8")
    index = html.find('</title>')
    end = index if index > 512 else 512
    content = html[:end]  # in order to consume less cpu
    try:
        dom = lxml.html.fromstring(content.decode('utf8', 'ignore'), \
                                   parser=lxml.html.HTMLParser(remove_comments=True))
        encs = dom.xpath('.//head/meta[@charset]/@charset')
        encs += [re.findall(r'charset=(.*)', _.get('content'))[0] \
                 for _ in dom.xpath('.//head/meta[@http-equiv][@content]') \
                 if _.get('http-equiv').lower() == "content-type" and _.get('content').count('charset=') == 1]
        encs = set([_.lower() for _ in encs])

        if set(['gb2312', 'gbk']) <= encs:
            encs.remove('gb2312')
        if set(['gb2312']) == encs:
            encs = set(['gbk'])

        if len(encs) == 1:
            charset = encs.pop()

            import codecs
            codecs.lookup(charset)  # raise exception if charset is unknown

    except Exception:
        charset = None
    finally:
        if charset is None:
            # no encoding or multiple encoding(for web-cache sites)
            import chardet
            content = bytes(content, encoding="utf8")
            result = chardet.detect(content)
            charset = result['encoding'] if result['confidence'] >= 0.8 else 'gbk'
        return charset


class WrappedResponse(object):
    def __init__(self, status_code=0, error_code=0, headers={}, content='', cookies={}, history=[], \
                 encoding=None, raw_headers='', total_time=0, reason=None, version=0, **kwargs):
        self._status_code = status_code
        self._error_code = error_code
        self._headers = dict(headers)
        self._raw_content = content
        self._content = None
        self._cookie = dict(cookies)
        self._history = history
        self._encoding = encoding
        self._used_time = 0
        self._raw_headers = raw_headers
        self._total_time = total_time
        self._reason = reason
        self._version = version

    @property
    def used_time(self):
        return self._used_time

    @used_time.setter
    def used_time(self, used_time):
        self._used_time = used_time

    @property
    def total_time(self):
        return self._total_time

    @property
    def status_code(self):
        return self._status_code

    @property
    def error_code(self):
        return self._error_code

    @property
    def version(self):
        return self._version

    @property
    def headers(self):
        return self._headers

    @property
    def raw_headers(self):
        return self._raw_headers

    # @exe_time
    def _2utf8(self):
        content = None
        try:
            if self._raw_content and _is_text_response(self._headers):
                encoding = self.encoding
                if encoding != 'utf-8' and encoding != 'utf8':
                    content = self._raw_content.decode(encoding, 'ignore').encode('utf-8', 'ignore')
        except:
            logger.debug(traceback.format_exc())
        return content

    @property
    def content(self):
        if self._content is None:
            self._content = self._2utf8() or self._raw_content

        return self._content

    @property
    def cookies(self):
        return self._cookie

    @property
    def reason(self):
        return self._reason

    @property
    def history(self):
        return self._history

    @property
    def encoding(self):
        if self._encoding is None:
            encoding = _get_encoding(self._headers, self._raw_content)
            if encoding:
                self._encoding = encoding.lower()
        return self._encoding

    def is_reachable(self):
        return not ((self.status_code / 100 == 6 and self.error_code > 0) or self.status_code == 407)

    def __str__(self):
        return '<%s %d>' % (self.__class__.__name__, self.status_code)


if __name__ == '__main__':
   w= WrappedUrl('http://www.baidu.com')
   print(w.schema)
