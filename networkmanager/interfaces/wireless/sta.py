from networkmanager import NetworkManager
from networkmanager.interfaces.wireless import Wireless
from network import WLAN, STA_IF

class STA(Wireless):
    def __init__(self):
        self._interface = WLAN(STA_IF)


    @property
    def channel(self):
        return self._interface.config('channel')


    @property
    def ssid(self):
        return self._interface.config('ssid')


    @property
    def reconnects(self):
        return self._interface.config('reconnects')


    @reconnects.setter
    def reconnects(self, value):
        _interface.config(reconnects=value)


NetworkManager.register_interface('wlanSTA', STA)
