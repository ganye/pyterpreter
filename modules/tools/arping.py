from base.module import Module
from scapy.all import Ether, ARP, srp, conf
import os
import time

class Arping(Module):
    def initialize(self):
        self.update_info({
            'name' : 'Arping',
            'description' : 'Simple module to send an ARP out to the whole' +
                            'network and prints the results.',
            'license' : 'BSD',
            'author' : ['ganye'],
        })
        self.set_options({
            'network' : [True, 'The network to scan for responses.',]
        })

    def run(self):
        conf.verb = 0
        self.console.writeln("[+] sending arping...")
        ans, unans = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/
                         ARP(pdst=self.network.get()),timeout=2)

        self.console.writeln("[+] done")
        rows, columns = (-1, -1)
        split_input = True
        try:
            # Get the size of the window. We really only care about the rows -
            # this is used for formatting large amounts of data
            rows, columns = os.popen('stty size', 'r')
        except Exception:
            self.console.warn("couldn't get the terminal window size - " +
                                "printing without formatting.")
            time.sleep(2)
            split_input = False

        counter = 0
        for snd, rcv in ans:
            if counter == 0:
                self.console.writeln("MAC\t\t\tIP")
                counter += 1
            elif counter == rows and split_input:
                # TODO: Make this more framework-friendly
                raw_input("Press any key to continue.")
                counter = 0
            self.console.writeln(rcv.sprintf("%Ether.src%\t%ARP.psrc%"))
            counter += 1
