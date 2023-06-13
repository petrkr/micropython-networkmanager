
class Interface():
    def __init__(self):
        self._ev_connecting = []
        self._ev_connected = []
        self._ev_disconnected = []


    def _connect(self):
        raise NotImplementedError()


    def _disconnect(self):
        raise NotImplementedError()


    @property
    def isconnected(self):
        return self._interface.isconnected()


    def connect(self, *args, **kargs):
        self._connect(*args, **kargs)


    def disconnect(self):
        self._disconnect()


    def ifconfig(self):
        return self._interface.ifconfig()


    # If interface need, do some loop stuff in this method
    def loop(self):
        pass
