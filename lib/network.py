import socket
import struct
import fcntl

__all__ = ["get_mac",]

def get_mac(ifname):
    """
    Returns the MAC address for the giving interface.
    Ex:
    >>> get_mac('wlp2s0')
    00:00:de:ad:be:ef
    >>>
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    info = fcntl.ioctl(s.fileno(), 0x8927, struct.pack('256s', ifname[:15]))
    return ''.join(['%02x:' % ord(char) for char in info[18:24]])[:-1]