import sys


class System(object):
    def __init__(self):
        self.platform = sys.platform
        self._config = Config()
        self._wurl = None

    @property
    def config(self):
        return self._config

    @config.setter
    def config(self, config):
        self._config = config

    @property
    def wurl(self):
        return self._wurl

    @wurl.setter
    def wurl(self, wurl):
        self._wurl = wurl


class Config(object):
    def __init__(self):
        self._port_plugin_id = None
        self._whois_plugin_id = None

    @property
    def port_plugin_id(self):
        return self._port_plugin_id

    @port_plugin_id.setter
    def port_plugin_id(self, port_plugin_id):
        self._port_plugin_id = port_plugin_id
