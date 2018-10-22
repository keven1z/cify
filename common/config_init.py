#########################################################
# (C)  zii .All rights Reserved#
#########################################################

from xml.dom.minidom import parse
from common.wharehouse import Wharehouse
from common.log.logUtil import LogUtil as logging
from common.moudle.cdn_check import CDNDetect
import sys

logger = logging.getLogger(__name__)
PLUGINS = 'plugins'
SPIDERS = 'spiders'
PORT = 'port'
ID = 'id'


def read():
    dom = parse("config.xml")
    # 获取文件元素对象
    warehouse = Wharehouse()
    document = dom.documentElement
    plugins_nodes = document.getElementsByTagName(PLUGINS)[0]
    spider_nodes = document.getElementsByTagName(SPIDERS)[0]
    try:
        for element in plugins_nodes.childNodes:
            if element.nodeName == PORT:
                for node in element.childNodes:
                    if node.nodeName == ID:
                        port_plugin_id = node.childNodes[0].data
                        warehouse.config.port_plugin_id = port_plugin_id
        for element2 in spider_nodes.childNodes:
            if element2.nodeName == PORT:
                for node2 in element2.childNodes:
                    if node2.nodeName == ID:
                        port_spider_id = node2.childNodes[0].data
                        warehouse.config.port_spider_id = port_spider_id
    except Exception as e:
        logger.error('config load error')
        sys.exit(0)
    return warehouse


def banner():
    _banner = "       _____ ________ \n" + "__________(_)___  __/_____  __\n" + "_  ___/__  / __  /_  __  / / /\n" + "/ /__  _  /  _  __/  _  /_/ / \n" + "\___/  /_/   /_/     _\__, /  \n" + "                     /____/  "
    _banner = _banner + 'Copyright [2018.9-2018.11] [zii]'
    print(_banner)


def cdn_check(host):
    cdn = CDNDetect(host)
    is_cdn, ip, cdn_name = cdn._check()
    if is_cdn:
        logger.debug('The URL has cdn ,can\'t scan' )
        sys.exit(0)
    else:
        return ip
