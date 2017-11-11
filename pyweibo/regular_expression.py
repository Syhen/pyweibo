# -*- coding: utf-8 -*-
"""
create on 2017-11-04 下午3:20

author @heyao
"""

import re

RE_FM_CONTENT = re.compile(r"<script>FM\.view\((.*?)\)</script>")
RE_MAIN_CONTENT = re.compile(r"<body>([\s\S]*?)</body>")
