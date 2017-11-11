# -*- coding: utf-8 -*-
"""
create on 2017-06-19 上午12:13

author @heyao
"""


class Response(object):
    def __init__(self, response):
        self._response = response
        self.init_response()

    def init_response(self):
        for key in self._response.__dict__:
            if not key.startswith('_'):
                setattr(self, key, self._response.__dict__[key])
