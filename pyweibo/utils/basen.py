# -*- coding: utf-8 -*-
"""
create on 2017-06-19 上午12:35

author @heyao
"""

import base64


def bnencode(string, mode=64):
    if mode not in (16, 32, 64):
        raise ValueError("'mode' must in (16, 32, 64)")
    return getattr(base64, 'b%sencode' % mode)(string)


def bndecode(string, mode=64):
    if mode not in (16, 32, 64):
        raise ValueError("'mode' must in (16, 32, 64)")
    return getattr(base64, 'b%sdecode' % mode)(string)
