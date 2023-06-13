from networkmanager import NetworkManager
from networkmanager.interfaces.wireless import Wireless
from network import WLAN, STA_IF

class STA(Wireless):
    def __init__(self):
        self._interface = WLAN(STA_IF)


    def _connect(self, *args, **kargs):
        self._interface.connect(*args, **kargs)


    def _disconnect(self):
        self._interface.disconnect()


    @property
    def channel(self):
        return self._interface.config('channel')


    @property
    def reconnects(self):
        return self._interface.config('reconnects')


    @property
    def rssi(self):
        return self._interface.status('rssi')


    @reconnects.setter
    def reconnects(self, value):
        _interface.config(reconnects=value)


NetworkManager.register_interface('wlanSTA', STA)
