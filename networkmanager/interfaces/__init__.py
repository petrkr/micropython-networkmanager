
class Interface():
    def __init__(self):
        self._ev_connecting = []
        self._ev_connected = []
        self._ev_disconnected = []


    @property
    def isconnected(self):
        return self._interface.isconnected()


    def connect(self):
        raise NotImplementedError()


    def disconnect(self):
        raise NotImplementedError()


    def ifconfig(self):
        return self._interface.ifconfig()


    # If interface need, do some loop stuff in this method
    def loop(self):
        pass
