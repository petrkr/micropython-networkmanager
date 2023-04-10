import network
import ujson as json
import uos as os
import urequests as requests
import uerrno as errno

class NetworkManager:
    def __init__(self, config_file='network_config.json'):
        self.config_file = config_file
        self.config = None
        self.interfaces = {}

    def load_config(self):
        try:
            with open(self.config_file) as f:
                self.config = json.load(f)
        except OSError:
            print('Error: Could not open configuration file.')
            return

        for interface in self.config['interfaces']:
            if interface['type'] == 'eth':
                self.interfaces[interface['name']] = network.LAN(interface['pin'])
            elif interface['type'] == 'wifi_sta':
                wlan = network.WLAN(network.STA_IF)
                wlan.active(True)
                for network_config in interface['networks']:
                    ssid = network_config['ssid']
                    password = network_config['password']
                    wlan.add_network(ssid, password)
                self.interfaces[interface['name']] = wlan
            elif interface['type'] == 'wifi_ap':
                self.interfaces[interface['name']] = network.WLAN(network.AP_IF)
                self.interfaces[interface['name']].active(True)
                self.interfaces[interface['name']].config(essid=interface['ssid'], password=interface['password'])
            elif interface['type'] == 'pppos':
                self.interfaces[interface['name']] = network.PPP(interface['uart'], interface['apn'], interface['user'], interface['password'])

    def save_config(self):
        try:
            with open(self.config_file, 'w') as f:
                json.dump(self.config, f)
        except OSError:
            print('Error: Could not save configuration file.')

    def add_interface(self, interface):
        if interface['type'] == 'eth':
            self.interfaces[interface['name']] = network.LAN(interface['pin'])
        elif interface['type'] == 'wifi_sta':
            self.interfaces[interface['name']] = network.WLAN(network.STA_IF)
        elif interface['type'] == 'wifi_ap':
            self.interfaces[interface['name']] = network.WLAN(network.AP_IF)
        elif interface['type'] == 'pppos':
            self.interfaces[interface['name']] = network.PPP(interface['uart'], interface['apn'], interface['user'], interface['password'])

        self.config['interfaces'].append(interface)

    def remove_interface(self, interface_name):
        try:
            interface = next(interface for interface in self.config['interfaces'] if interface['name'] == interface_name)
            self.config['interfaces'].remove(interface)
            del self.interfaces[interface_name]
        except StopIteration:
            print('Error: Interface not found.')

    def get_interface(self, interface_name):
        if interface_name in self.interfaces:
            return self.interfaces[interface_name]
        else:
            print('Error: Interface not found.')

    def get_interfaces(self):
        return self.interfaces

    def configure(self):
        # Configuration plugin interface goes here
        pass

    def start(self):
        if self.config is None:
            self.load_config()

        for interface_name, interface in self.interfaces.items():
            if isinstance(interface, network.WLAN):
                while not interface.isconnected():
                    pass

            print('Interface {} started.'.format(interface_name))

    def stop(self):
        for interface_name, interface in self.interfaces.items():
            if isinstance(interface, network.WLAN):
                interface.disconnect()

            print('Interface {} stopped.'.format(interface_name))
