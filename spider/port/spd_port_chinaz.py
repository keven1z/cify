from common.net.webUtil import Web
from common.spider import Spider
from common.log.logUtil import LogUtil as logging
from spider.port.constant import PortConstant
from common.net.proxy.ipproxy import IPProxy
from concurrent.futures import ThreadPoolExecutor

logger = logging.instance().getLogger()
logger.setLevel(logging.ERROR)


class CifySpider(Spider):
    def __init__(self):
        super(CifySpider, self).__init__()
        self.s_id = 10000
        self._url = 'http://tool.chinaz.com/iframe.ashx?t=port&callback='  # chinaz的接口
        self.client = Web()
        self.port_status = {}
        self.proxy = IPProxy()
        self._target = None

    def _run(self, system):
        port_array = PortConstant.PORTARRAY
        self._target = system.wurl.hostname
        thread_num = len(port_array) / 2 + 1
        with ThreadPoolExecutor(thread_num) as executor:
            for port in port_array:
                executor.submit(self.getPortStatus, port)

    def getPortStatus(self, port):
        url = self._url
        data = []
        hostlist = ['host', self._target]
        hostlist = tuple(hostlist)
        portlist = ['port', port]
        portlist = tuple(portlist)

        ip = self.proxy.generate()
        proxies = {'http': ip}
        encode = ['encode', 'IxGn5ej1ogzYmxJNUQI|NwA2YxLV2WRq']
        encode = tuple(encode)
        data.append(hostlist)
        data.append(portlist)
        data.append(encode)
        resp = self.client.request('POST', url, data=data, proxies=proxies, timeout=8.0)
        if resp is None:
            self.getPortStatus(port)
        status = self.filter(resp.text)
        self.port_status[port] = status

    def filter(self, content):
        if content.find('html') == -1:
            status = content[9:10]
            if status == '1':
                return PortConstant.OPEN
            elif status == '0':
                return PortConstant.CLOSE
        else:
            return PortConstant.UNKONWN

    def report(self):
        print(self.port_status)


if __name__ == '__main__':
    spd = CifySpider()
    host = '39.108.133.111'
    spd.run(host)
