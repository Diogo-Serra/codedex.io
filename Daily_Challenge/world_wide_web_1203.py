#!/usr/bin/env python3
import string


def check_url(address):
    valid_domain_chars = string.ascii_letters + string.digits + "-."

    # Rule 1: must start with http:// or https://
    if address.startswith("https://"):
        domain = address[len("https://"):]
    elif address.startswith("http://"):
        domain = address[len("http://"):]
    else:
        return "invalid"

    # Rule 2: domain must contain at least one dot
    if "." not in domain:
        return "invalid"

    # Rule 3: domain only contains letters, digits, hyphens, or dots
    if not all(c in valid_domain_chars for c in domain):
        return "invalid"

    return "valid"
