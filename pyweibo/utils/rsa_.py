# -*- coding: utf-8 -*-
"""
create on 2017-06-19 上午12:37

author @heyao
"""

from __future__ import unicode_literals

import rsa


class Rsa(object):
    def __init__(self):
        pass

    def key_from_n16(self, n16, e=65537):
        n = int(n16, 16)
        return rsa.PublicKey(n, e)

    def key_from_(self):
        pass

    def encrypt(self, string, public_key):
        return rsa.encrypt(str(string), public_key)

    def decrypt(self, crypto, private_key):
        return rsa.decrypt(str(crypto), private_key)
