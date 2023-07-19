from networkmanager.interfaces.ethernet import Ethernet
from network import LAN, PHY_LAN8720, ETH_CLOCK_GPIO17_OUT
from machine import Pin

class W5500(Ethernet):
    def __init__(self, spi):
        raise NotImplementedError()
