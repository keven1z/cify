#########################################################
# (C)  zii .All rights Reserved#
#########################################################


from common.wharehouse import Wharehouse
from common.moudle.cdn_detect import CDNDetect
from common.utils.printdata import *
from error.CDNQueryError import CDNQueryError
from common.moudle.waf_detect import WafDetect
from data.config import *
import xml.etree.ElementTree as ET
import os
import traceback
import sys

logger = log.getLogger(__name__)
PORT = 'port'
WHOIS = 'whois'
CMS = 'cms'
ID = 'id'


def read():
    try:
        warehouse = Wharehouse()
        target_dict = {}
        tree = ET.parse(os.getcwd() + '/' + CONFIG_FILE_PATH)
        for elems in tree.iterfind('plugins/plugin'):
            type = elems.get('type')
            ele_dict = {}
            for elem in list(elems):
                ele_dict[elem.tag] = elem.text
            target_dict[type] = ele_dict
        id = target_dict[PORT][ID]
        warehouse.config.port_plugin_id = id
        id = target_dict[WHOIS][ID]
        warehouse.config.whois_plugin_id = id
        id = target_dict[CMS][ID]
        warehouse.config.cms_id = id
        return warehouse
    except IndexError as e:
        info('Initialize configuration failed')
        logger.error('Initialize configuration failed')
        logger.error(traceback.format_exc())
        sys.exit(0)


def banner():
    _banner = "       _____ ________ \n" \
              "__________(_)___  __/_____  __\n" \
              "_  ___/__  / __  /_  __  / / /\n" \
              "/ /__  _  /  _  __/  _  /_/ / \n" \
              "\___/  /_/   /_/     _\__, /  \n" \
              "                     /____/  \n"
    _banner = _banner + 'Copyright [' + TIME + '] [' + AUTHOR + ']'
    print(_banner)
    print()
    info('Starting CIFY 1.1  ')


def cdn_check(host):
    cdn = CDNDetect(host)
    try:
        ip = cdn.run()
        return ip
    except CDNQueryError as e:
        error('CDN check failed,reason:' + e.__str__())
        logger.error('CDN check failed,reason:' + e.__str__())


def waf_check(wharehouse):
    waf = WafDetect(wharehouse)
    waf_name = waf.run()
    return waf_name
