from xml.dom.minidom import parse
from common.log.logUtil import LogUtil as logging
import sys
from common.net.webUtil import Web
from common.net.proxy.rulermanager import RulerManager
import random
import os
logger = logging.instance().getLogger()


class IPProxy(object):
    def __init__(self):
        self.config_path = os.path.dirname(__file__)+'/config_ruler.xml'
        self.rulerManager = RulerManager()
        self.ip_list = []
        self.web = Web()

    def generate(self):  # 生成ip代理ip池
        ruler_id, url = self.config_read()
        self.ip_list = self.get_ip_list(url, ruler_id)
        proxy_ip = self.get_random_ip()
        return proxy_ip

    def get_ip_list(self, url, ruler_id):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
        }
        resp = self.web.request('GET', url, iscache=True, headers=headers)
        web_text = resp.text
        self.rulerManager.load()
        ruler_list, ruler_hash = self.rulerManager.get_modules()
        ruler_obj = ruler_hash[ruler_id].module_obj
        ruler_obj.execute(web_text)
        ip_list = ruler_obj.get_ip_list()
        return ip_list

    def get_random_ip(self):
        ip_list = self.ip_list
        proxy_ip = random.choice(ip_list)
        return proxy_ip

    def config_read(self):
        try:
            dom = parse(self.config_path)
            # 获取文件元素对象
            document = dom.documentElement
            module_list = document.getElementsByTagName("module")
            # 获取ip
            ruler_list = module_list[0].getElementsByTagName("id")
            url_list = module_list[0].getElementsByTagName("url")
            ruler_id = ruler_list[0].childNodes[0].data
            url = url_list[0].childNodes[0].data
        except Exception as e:
            logger.error('IP proxy config read error')
            sys.exit()

        return ruler_id, url


if __name__ == '__main__':
    ipproxy = IPProxy()
    ip = ipproxy.generate()
    print(ip)
