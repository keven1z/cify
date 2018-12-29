import os
from functools import partial
from common.net.webUtil import Request
from pluginbase import PluginBase
import re
import random
import copy
import urllib.parse
from common.log.log_util import LogUtil as log
from common.utils.printdata import *
from common.threads.thread_pool import ThreadPool

logger = log.getLogger(__name__)


class WafDetect(object):
    AdminFolder = '/Admin_Files/'
    xss_string = '<script>alert(1)</script>'
    dir_travel_string = '../../../../etc/passwd'
    clean_html_string = '<invalid>hello'
    isaservermatch = [
        'Forbidden ( The server denied the specified Uniform Resource Locator (URL). \
        Contact the server administrator.  )',
        'Forbidden ( The ISA Server denied the specified Uniform Resource Locator (URL)']

    def __init__(self, wharehouse):
        self.wharehouse = wharehouse
        self.client = Request()
        self.path = '/'
        self.threadPool = ThreadPool()
        self.flag = False

    def request(self, method=None, path=''):
        wurl = self.wharehouse.wurl
        w_url = copy.deepcopy(wurl)
        w_url.method = method
        w_url.url += path
        w_resp = self.client.request(w_url)
        return w_resp

    def normal_request(self, headers=None):
        wurl = self.wharehouse.wurl
        w_url = copy.deepcopy(wurl)
        w_url.headers = headers
        w_resp = self.client.request(w_url)
        return w_resp

    def normal_non_existent_file(self):
        wurl = copy.deepcopy(self.wharehouse.wurl)
        path = '/' + str(random.randrange(1000, 9999)) + '.html'
        wurl.url += wurl.url + path
        w_resp = self.client.request(wurl)
        return w_resp

    def unknown_method(self):
        wurl = copy.deepcopy(self.wharehouse.wurl)
        wurl.method = 'ZII'
        return self.client.request(wurl)

    def directory_traversal(self):
        w_url = copy.deepcopy(self.wharehouse.wurl)
        w_url.url = w_url.url + '/' + self.dir_travel_string
        return self.client.request(w_url)

    def invalid_host(self):
        random_number = random.randrange(100000, 999999)
        wurl = copy.deepcopy(self.wharehouse.wurl)
        wurl.headers = {'Host': str(random_number)}
        resp = self.client.request(wurl)
        return resp

    def clean_html_encoded(self):
        string = '/' + urllib.parse.quote(self.clean_html_string) + '.html'
        wurl = copy.deepcopy(self.wharehouse.wurl)
        wurl.url += string
        return self.client.request(wurl)

    def clean_html(self):
        string = '/' + self.clean_html_string + '.html'
        wurl = copy.deepcopy(self.wharehouse.wurl)
        wurl.url += string
        return self.client.request(wurl)

    def xss_standard(self):
        string = '/' + self.xss_string + '.html'
        wurl = copy.deepcopy(self.wharehouse.wurl)
        wurl.url += string
        return self.client.request(wurl)

    def protected_folder(self):
        string = '/' + self.AdminFolder
        wurl = copy.deepcopy(self.wharehouse.wurl)
        wurl.url += string
        return self.client.request(wurl)

    def xss_standard_encoded(self):
        string = '/' + urllib.parse.quote(self.xss_string) + '.html'
        wurl = copy.deepcopy(self.wharehouse.wurl)
        wurl.url += string
        return self.client.request(wurl)

    def cmd_dot_exe(self):
        # thanks j0e
        string = '/' + 'cmd.exe'
        w_url = copy.deepcopy(self.wharehouse.wurl)
        w_url.url += string
        return self.client.request(w_url)

    attacks = [cmd_dot_exe, directory_traversal, xss_standard, protected_folder, xss_standard_encoded]

    def load_plugins(self):
        try:
            here = os.path.abspath(os.path.dirname(__file__))
            get_path = partial(os.path.join, here)
            plugin_dir = get_path('waf_plugins')

            plugin_base = PluginBase(
                package='waf_plugins', searchpath=[plugin_dir]
            )
            plugin_source = plugin_base.make_plugin_source(
                searchpath=[plugin_dir], persist=True
            )
            plugin_dict = {}
            for plugin_name in plugin_source.list_plugins():
                plugin_dict[plugin_name] = plugin_source.load_plugin(plugin_name)
            return plugin_dict
        except Exception as e:
            logging.error('Load waf plugins failed ' + str(e))
        return None

    def match_header(self, header, attack=False):
        header_name, match = header
        if attack:
            for attack in self.attacks:
                w_resp = attack(self)
                if w_resp is None:
                    return
                header_val = w_resp.headers.get(header_name) or w_resp.headers.get(header_name.lower())
                if header_val:
                    if header_name == 'Set-Cookie':
                        header_vals = header_val.split(', ')
                    else:
                        header_vals = [header_val]
                    for header_val in header_vals:
                        if re.match(match, header_val, re.IGNORECASE):
                            return True
        else:
            w_resp = self.normal_request()
            if w_resp is None:
                return
            header_val = w_resp.headers.get(header_name)
            if header_val:
                if header_name == 'Set-Cookie':
                    header_vals = header_val.split(', ')
                else:
                    header_vals = [header_val]
                for header_val in header_vals:
                    if re.search(match, header_val, re.IGNORECASE):
                        return True
        return False

    def match_cookie(self, match):
        return self.match_header(('Set-Cookie', match))

    def check_waf(self, plugins_fuc, plugin_name):
        if plugins_fuc.is_waf(self):
            logging.info('Found waf,name:' + plugin_name)
            info('Found waf,name:' + plugins_fuc.NAME)
            self.flag = True
            self.threadPool.clear_tasks()

    def run(self):
        plugins_dict = self.load_plugins()
        if plugins_dict is not None:
            info('Checking WAF')
            for plugin_name, plugins_fuc in plugins_dict.items():
                self.threadPool.add_task(self.check_waf, plugins_fuc, plugin_name)
        self.threadPool.wait_all_complete()
        if not self.flag:
            logging.info('The ' + self.wharehouse.wurl.url + ' is probably not WAF')
            info('The ' + self.wharehouse.wurl.url + ' is probably not WAF')
            return None


if __name__ == '__main__':
    from common.wharehouse import Wharehouse
    from common.net.url import WrappedUrl

    s = time.time()
    w = WrappedUrl('http://www.safedog.cn/')
    whare = Wharehouse()
    whare.wurl = w
    WafDetect(whare).run()
    warn('使用了' + str(time.time() - s))
