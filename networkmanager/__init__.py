# Network Manager

__version__ = "0.0.1"
__license__ = "MIT"

class NetworkManager:
    _instance = None
    _interface_types = dict()
    _interfaces = dict()


    def __new__(cls):
        if cls._instance:
            return cls._instance

        # New singleton instance
        cls._instance = super(NetworkManager, cls).__new__(cls)

        # Event list
        cls._ev_connecting = []
        cls._ev_connected = []
        cls._ev_disconnected = []
        cls._ev_timeout = []

        return cls._instance


    @classmethod
    def register_interface(cls, iftype, interface):
        if iftype in cls._interface_types:
            raise ValueError("Interface type {} already exists".format(iftype))

        cls._interface_types[iftype] = interface


    def create_interface(self, iftype, ifname, *args, **kargs):
        if ifname in self._interfaces:
            raise ValueError("Interface {} already exists".format(ifname))

        if iftype not in self._interface_types:
            raise ValueError("Interface type {} does not exists, did you imported it?".format(iftype))

        self._interfaces[ifname] = self._interface_types[iftype](*args, **kargs)


    def delete_interface(self, ifname):
        if ifname not in self._interfaces:
            raise ValueError("Interface {} does not exists".format(ifname))

        # TODO: some free / deregister? Like disconnect etc?
        del self._interfaces[ifname]


    # TODO: Really do it like that?
    @property
    def interface_types(self):
        return self._interface_types


    def interface(self, ifname=None):
        if ifname is None:
            return self._interfaces

        if ifname not in self._interfaces:
            raise ValueError("Interface {} does not exists".format(ifname))

        return self._interfaces[ifname]


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


    # Main loop - or create internal thread instead?
    def loop(self):
        pass
