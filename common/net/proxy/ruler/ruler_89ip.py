import re
from common.net.proxy.ruler.ruler import Ruler


class CifyRuler(Ruler):
    def __init__(self):
        super(CifyRuler, self).__init__()
        self.ruler_id = 10000
        self.ip_list=[]

    def _execute(self, html_text):
        pattern = '[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+:[0-9]+'
        self.ip_list = re.findall(pattern, html_text)

    def get_ip_list(self):
        return self.ip_list

