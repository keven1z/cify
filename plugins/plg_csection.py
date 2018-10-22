#########################################################
# (C)  zii .All rights Reserved#
#########################################################

import sys
from common.plugin import Plugin
from common.log.logUtil import LogUtil as logging

logging = logging.getLogger(__name__)


class CifyPlugin(Plugin):
    def __init__(self):
        super(CifyPlugin, self).__init__()
        self._id = 10002

    def _run(self):
        pass
