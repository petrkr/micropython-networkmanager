# Network Manager

__version__ = "0.0.1"
__license__ = "MIT"

class NetworkManager:
    _interfaceTypes = list()

    def __init__(self):
        # Event list
        self._ev_connecting = []
        self._ev_connected = []
        self._ev_disconnected = []
        self._ev_timeout = []

        self._interfaces = list()

        # Create instance of known interfaces
        # TODO: Maybe create only active ones to save memory?
        for i in self._interfaceTypes:
            self._interfaces.append(i())


    @classmethod
    def register_interface(cls, interface):
        cls._interfaceTypes.append(interface)


    def _connect(self):
        pass


    def _ev_connecting(self, iface, retry):
        for f in self._events_connecting:
            f(iface, retry)


    def _ev_connected(self, iface):
        for f in self._events_connected:
            f(iface)


    def _ev_disconnected(self, iface):
        for f in self._events_disconnected:
            f(iface)


    def _ev_timeout(self, iface):
        for f in self._events_timeout:
            f(iface)


    def event_add_connecting(self, func):
        self._ev_connecting.append(func)


    def event_add_connected(self, func):
        self._ev_connected.append(func)


    def event_add_disconnected(self, func):
        self._ev_disconnected.append(func)


    def event_add_timeout(self, func):
        self._ev_timeout.append(func)


    def available_interfaces(self):
        return self._interfaceTypes


    def interfaces(self):
        return self._interfaces


    # Main loop - or create internal thread instead?
    def loop(self):
        pass
