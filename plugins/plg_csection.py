#########################################################
# (C)  zii .All rights Reserved#
#########################################################
from IPy import IP as IPyer
from common.plugin import Plugin
from common.log.logUtil import LogUtil as logging
from kamene.route import *
from kamene.layers.inet import sr1, IP, TCP

logging = logging.getLogger(__name__)


class CifyPlugin(Plugin):
    def __init__(self):
        super(CifyPlugin, self).__init__()
        self._id = 10002
        self.ip = None
        self.ip_list = []
        self.ip_alive_list = []

    def _run(self):
        self._get_c_section()
        self._syn_send()

    def _syn_send(self):
        for ip in self.ip_list:
            try:
                p = sr1(IP(dst=ip) / TCP(dport=80, flags="S"), timeout=5, verbose=False)
                if p:
                    self.ip_alive_list.append(ip)
                    logging.debug('Found a alive host, ip:' + ip)
            except Exception as e:
                logging.error(str(e))

    def _get_c_section(self):
        self.ip = self.wharehouse.ip
        ip = IPyer(self.ip).make_net('255.255.255.0')
        ips = IPyer(ip)
        [self.ip_list.append(x) for x in ips]


if __name__ == '__main__':
    from common.wharehouse import Wharehouse

    wharehouse = Wharehouse()
    wharehouse.ip = '39.108.133.110'
    CifyPlugin().run(wharehouse)
