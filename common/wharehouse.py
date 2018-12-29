#########################################################
# (C)  zii .All rights Reserved#
#########################################################

import sys


class Wharehouse(object):
    def __init__(self):
        self.platform = sys.platform
        self._config = Config()
        self._wurl = None
        self._ip = None

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

    @property
    def ip(self):
        return self._ip

    @ip.setter
    def ip(self, ip):
        self._ip = ip


class Config(object):
    def __init__(self):
        self._port_plugin_id = None
        self._whois_plugin_id = None
        self._cms_id = None

    @property
    def port_plugin_id(self):
        return self._port_plugin_id

    @port_plugin_id.setter
    def port_plugin_id(self, port_plugin_id):
        self._port_plugin_id = port_plugin_id



    @property
    def whois_plugin_id(self):
        return self._whois_plugin_id

    @whois_plugin_id.setter
    def whois_plugin_id(self, whois_plugin_id):
        self._whois_plugin_id = whois_plugin_id

    @property
    def cms_id(self):
        return self._cms_id

    @cms_id.setter
    def cms_id(self, cms_id):
        self._cms_id = cms_id
