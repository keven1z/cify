# __*__coding:utf-8__*__
#######################
# 扫描端口插件
#######################
from common.plugin import Plugin
from lib.nmap.nmap3.nmap3 import Nmap,NmapScanTechniques
from common.utils.printdata import *

logger = log.getLogger(__name__)


class CifyPlugin(Plugin):

    def __init__(self):
        super(CifyPlugin, self).__init__()
        self._id = 10000

    def _run(self):
        try:
            wurl = self.wharehouse.wurl
            url = wurl.hostname
            report = self.do_scan(url)
            if report is not None:
                self.result = self.print_scan(report)
            else:
                return None
        except PermissionError as e:
            logger.error(e)

    def do_scan(self, target):
        info('Starting scaning port')
        try:
            # if current user is not root,use normal scan ,else use syn scan replace
            if os.geteuid() != 0:
                nmap = Nmap()
                return nmap.nmap_version_detection(target)
            else:
                return NmapScanTechniques().nmap_syn_scan(target)
        except KeyboardInterrupt:
            raise KeyboardInterrupt
        except Exception as e:
            logger.error(e)
            return None

    def print_scan(self, result):
        port_list = []
        for ip, v in result.items():
            for p in v:
                state = p['state']
                if 'version' not in p['service']:
                    p['service']['version'] = 'None'
                port_list.append({'port': p['port'], 'state': state, 'service_name': p['service']['name'],
                                  'version': p['service']['version']})
        return port_list
