# -*- coding: utf-8 -*-
"""
create on 2017-06-19 上午12:18

author @heyao
"""

from lxml import etree


class Selector(object):
    def __init__(self, response=None, text=u''):
        if response:
            encoding = response.encoding
            text = response.text.decode(encoding)
        self.selector = etree.HTML(text)

    def xpath(self, selector):
        return _ResultSet(self.selector.xpath(selector))


class _ResultSet(object):
    def __init__(self, result):
        self.result = result

    def __iter__(self):
        for i in self.result:
            yield i

    def __len__(self):
        return len(self.result)

    def extract(self):
        return self.result

    def extract_first(self, default=None):
        if self.result is None or len(self.result) == 0:
            return default
        return self.result[0]
