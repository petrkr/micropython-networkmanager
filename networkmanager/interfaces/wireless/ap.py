from networkmanager import NetworkManager
from networkmanager.interfaces.wireless import Wireless
from network import WLAN, AP_IF

class AP(Wireless):
    def __init__(self):
        self._interface = WLAN(AP_IF)


    @property
    def channel(self):
        return self._interface.config('channel')


    @channel.setter
    def channel(self, chan):
        self._interface.config(channel = chan)


    @property
    def ssid(self):
        return self._interface.config('ssid')


    @ssid.setter
    def ssid(self, value):
        return self._interface.config(ssid = value)


    @property
    def hidden(self):
        return self._interface.config('hidden')
    

    @hidden.setter
    def hidden(self, value):
        self._interface.config(hidden = value)


    @property
    def security(self):
        return self._interface.config('security')
    

    @security.setter
    def security(self, auth):
        self._interface.config(security = auth)


    @property
    def key(self):
        raise ValueError("Write-only property")


    @key.setter
    def key(self, value):
        self._interface.config(key = value)


NetworkManager.register_interface(AP)
NetworkManager.create_interface('wlanAP', AP)
