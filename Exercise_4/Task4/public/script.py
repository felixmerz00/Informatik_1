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
    if int(octet) <= 255 and int(octet) >= 0:
        return True
    else:
        return False


def is_valid_IPv4(ip: str):
    octets = ip.split(".")
    if len(octets) != 4:
        return False
    for octet in octets:
        if is_valid_IPv4_octet(octet) == False:
            return False
    return True


def is_valid_IPv6_hextet(hextet: str):
    hextet = int(hextet, 16)
    if hextet >= 0 and hextet <= 65152:
        return True
    else:
        return False


def is_valid_IPv6(ip: str):
    hextets = ip.split(":")
    if len(hextets) != 8:
        return False
    for hextet in hextets:
        if is_valid_IPv6_hextet(hextet) == False:
            return False
    return True


def is_valid_IP(ip: str):
    if "." in ip:
        return is_valid_IPv4(ip)
    elif ":" in ip:
        return is_valid_IPv6(ip)
    else:
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
