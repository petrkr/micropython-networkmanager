from networkmanager.interfaces.ethernet import Ethernet
from network import LAN, PHY_LAN8720, ETH_CLOCK_GPIO17_OUT
from machine import Pin

class LAN8720(Ethernet):
    def __init__(self, phy_addr = 1, clock_mode = ETH_CLOCK_GPIO17_OUT, mdc=23, mdio=18):
        self._interface = LAN(mdc = Pin(mdc), mdio=Pin(mdio), phy_type=PHY_LAN8720, phy_addr=phy_addr, clock_mode=clock_mode)
