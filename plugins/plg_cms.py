# __*__coding:utf-8__*__

#######################
# 检索url主机信息模块
#######################
from common.log.log_util import LogUtil as log
from common.plugin import Plugin
from functools import partial
from pluginbase import PluginBase
from common.net.webUtil import Request
from common.utils.printdata import *

logging = log.getLogger(__name__)


class CifyPlugin(Plugin):

    def __init__(self):
        super(CifyPlugin, self).__init__()
        self._id = 10004
        self.plugin_dict = {}
        self.load_plugins()
        self.http_client = Request()
        self.result = ResultExport.instance()

    def load_plugins(self):
        try:
            here = os.path.abspath(os.path.dirname(__file__))
            get_path = partial(os.path.join, here)
            plugin_dir = get_path('cms')

            plugin_base = PluginBase(
                package='waf_plugins', searchpath=[plugin_dir]
            )
            plugin_source = plugin_base.make_plugin_source(
                searchpath=[plugin_dir], persist=True
            )
            plugin_dict = {}
            for plugin_name in plugin_source.list_plugins():
                plugin_dict[plugin_name] = plugin_source.load_plugin(plugin_name)
            self.plugin_dict = plugin_dict
        except Exception as e:
            logging.error('Load waf plugins failed ' + str(e))
        return None

    def _run(self):
        info('Checking cms')
        self.result.add_data('CMS:')
        for method in self.plugin_dict.values():
            cms = method.check(self, self.wharehouse.wurl)
            if cms is not None:
                info('Check type of cms:' + cms)
                self.result.add_data(cms)
                return
        info('Not checking cms')
        self.result.add_data('not')

    def _request(self, wurl):
        w_resp = self.http_client.request(wurl)
        return w_resp
