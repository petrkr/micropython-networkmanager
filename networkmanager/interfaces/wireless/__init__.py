from networkmanager.interfaces import Interface
import network


class ScanResult():
    _securities = dict()
    _securities[network.AUTH_OPEN] = "Open"
    _securities[network.AUTH_WPA_PSK] = "WPA PSK"
    _securities[network.AUTH_WPA_WPA2_PSK] = "WPA/WPA2 PSK"
    _securities[network.AUTH_WPA2_PSK] = "WPA2 PSK"

    def __init__(self, result):
        self._ssid = result[0].decode()
        self._bssid = result[1]
        self._channel = result[2]
        self._rssi = result[3]
        self._security = result[4]
        self._hidden = result[5]
    

    def _get_security_name(self, security):
        return self._securities[security] if security in self._securities else "Unknown ({})".format(security)


    def __repl__(self):
        return self.__str__()


    def __str__(self):
        return ("{} - {}ch {}dB {}").format(self._ssid, self._channel, self._rssi, self._get_security_name(self._security))


class Wireless(Interface):
    def __init__(self):
        pass


    @property
    def mac(self):
        return self._interface.config('mac')


    @property
    def txpower(self):
        return self._interface.config('txpower')


    def active(self, value=None):
        if value is not None:
            return self._interface.active(value)
        else:
            return self._interface.active()


    def scan(self):
        return [ScanResult(s) for s in self._interface.scan()]
