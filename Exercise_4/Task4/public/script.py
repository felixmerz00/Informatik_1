#!/usr/bin/env python3

# These are examples for valid and invalid inputs to your validation function
from contextlib import nullcontext


IPv4_STRING = "127.0.0.1"
IPv4_INVALID_STRING = "300.0.0.1"
IPv6_STRING = "2001:0db8:85a3:0000:0000:8a2e:0370:7334"
IPv6_INVALID_STRING = "2001:0db8:85a3:0000:0000:8a2e:0370:7334:7334"
INVALID_IP_STRING = "Some arbitrary string"

#`a.b.c.d` where `a`, `b`, `c`, and `d` are integers between 0 and 255.
def is_valid_IPv4_octet(octet: str):
    """Returns True if octet represents a valid IPv4 octet, False otherwise"""
    a = int(octet)
    if octet < 0 and 255 < octet:
        return False
    else:
        return True

def is_valid_IPv4(ip: str):
    """Returns True if ip represents a valid IPv4 address, False otherwise"""
    i = ip.find(".")
    a = ip[:i]
    ip = ip[i+1:]
    i = ip.find(".")
    b = ip[:i]
    ip = ip[i+1:]
    i = ip.find(".")
    c = ip[:i]
    ip = ip[i+1:]
    d = ip
    return is_valid_IPv4_octet(a) and is_valid_IPv4_octet(b) and is_valid_IPv4_octet(c) and is_valid_IPv4_octet(d)

def is_valid_IPv6_hextet(hextet: str):
    """Returns True if hextet represents a valid IPv6 hextet, False otherwise"""
    pass

def is_valid_IPv6(ip: str):
    """Returns True if ip represents a valid IPv6 address, False otherwise"""
    pass

def is_valid_IP(ip: str):
    """Returns True if ip represents a valid IPv4 or IPv6 address False otherwise"""
    if(':' in ip):
        ip_list = ip.split(':')
        return is_valid_IPv6(ip)
    elif('.' in ip):
        ip_list = ip.split('.')
        return is_valid_IPv4(ip)
    return False


# The following lines call is_valid_IP and print the result.
# This way you can check what it does.
# However, we encourage you to write tests, because then you
# can easily test many different values on every "Test & Run"!
print(
    f"{IPv4_STRING} is a valid IP Address:",
    is_valid_IP(IPv4_STRING))
print(
    f"{IPv4_INVALID_STRING} is a valid IP Address:",
    is_valid_IP(IPv4_INVALID_STRING),
)
print(
    f"{IPv6_STRING} is a valid IP Address:",
    is_valid_IP(IPv6_STRING))
print(
    f"{IPv6_INVALID_STRING} is a valid IP Address:",
    is_valid_IP(IPv6_INVALID_STRING),
)
print(
    f"{INVALID_IP_STRING} is a valid IP Address:",
    is_valid_IP(INVALID_IP_STRING),
)
