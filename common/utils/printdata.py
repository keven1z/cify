from termcolor import colored, cprint
from common.log.log_util import LogUtil as log
import os
from prettytable import PrettyTable

logging = log.getLogger(__name__)


def warn(string, flag="[!]"):
    cprint(flag + string, 'yellow')


def error(string, flag="[-]"):
    cprint(flag + string, 'red')


def info(string, flag="[+]", end='\n'):
    cprint(flag + string, 'green', end=end)


def export_to_file(result, url):
    filepath = os.getcwd() + '/data/result/' + url + '.json'
    file = open(filepath, 'w+')
    file.truncate()  # 清空文件内容
    file.write(result.__str__())
    file.close()


def print_result(url):
    import data.data as data
    result = data.RESULT
    export_to_file(result, url)
    table = PrettyTable(['项', '值'])
    for k, v in result.items():
        if 'port' == k:
            table_port = PrettyTable()
            table_port.title = k
            for p in v:
                title_list = []
                tab_list = []
                for key, value in p.items():
                    title_list.append(key)
                    tab_list.append(value)
                table_port.field_names = title_list
                table_port.add_row(tab_list)
            print(table_port)
        elif 'whois' == k:
            table_whois = PrettyTable()
            table_whois.title = k
            table_whois.field_names = ['项', '值']
            for key, value in v.items():
                if isinstance(value, list):
                    tmp = ''
                    for v in value:
                        tmp += v + '\n'
                    value = tmp[0:-2]
                table_whois.add_row([key, value])
            print(table_whois)
        else:
            table.add_row([k, v])
    print(table)


if __name__ == '__main__':
    import datetime
    r = {'CDN': '183.252.199.196', 'waf': 'Safedog(安全狗)', 'cms': None,
         'port': [{'port': '21', 'state': 'open', 'service_name': 'ftp', 'version': None},
                  {'port': '30', 'state': 'open', 'service_name': 'tcpwrapped', 'version': None},
                  {'port': '80', 'state': 'open', 'service_name': 'http', 'version': None},
                  {'port': '311', 'state': 'open', 'service_name': 'tcpwrapped', 'version': None},
                  {'port': '443', 'state': 'open', 'service_name': 'http', 'version': None},
                  {'port': '705', 'state': 'open', 'service_name': 'tcpwrapped', 'version': None},
                  {'port': '912', 'state': 'open', 'service_name': 'tcpwrapped', 'version': None},
                  {'port': '1055', 'state': 'open', 'service_name': 'tcpwrapped', 'version': None},
                  {'port': '1296', 'state': 'open', 'service_name': 'tcpwrapped', 'version': None},
                  {'port': '2034', 'state': 'open', 'service_name': 'tcpwrapped', 'version': None},
                  {'port': '5200', 'state': 'open', 'service_name': 'tcpwrapped', 'version': None},
                  {'port': '5566', 'state': 'open', 'service_name': 'tcpwrapped', 'version': None},
                  {'port': '6106', 'state': 'open', 'service_name': 'tcpwrapped', 'version': None},
                  {'port': '14238', 'state': 'open', 'service_name': 'tcpwrapped', 'version': None},
                  {'port': '32784', 'state': 'open', 'service_name': 'tcpwrapped', 'version': None},
                  {'port': '55055', 'state': 'open', 'service_name': 'tcpwrapped', 'version': None}],
         'whois': {'domain_name': 'safedog.cn', 'registrar': '阿里云计算有限公司（万网）',
                   'creation_date': 'datetime.datetime(2010, 9, 6, 12, 38, 38)',
                   'expiration_date': 'datetime.datetime(2026, 9, 6, 12, 38, 38)',
                   'name_servers': ['f1g1ns1.dnspod.net', 'f1g1ns2.dnspod.net'], 'status': 'ok',
                   'emails': 'zhangzhx@safedog.cn', 'dnssec': 'unsigned', 'name': '厦门服云信息科技有限公司'}}
    import json
    print(json.dumps(r))
