# pyweibo
crawler for weibo.com

## Overview
API for weibo.com.

## Install
***目前尚未支持安装***
``` commandline
git clone https://github.com/heyaoyao/pyweibo.git
cd pyweibo
python setup.py install
```

## Requirements
rsa >= 3.4.2
lxml >= 3.7.3
requests
Python2.7

## Documentation
### quick start
```python
from pyweibo.http import weibo_downloader
url = 'http://weibo.com/u/2662018234'
response = weibo_downloader.download(url)
```

## Classes
> ### class pyweibo.parser.parse_response
微博页面解析器

> ### class pyweibo.selector.Selector
通过xpath解析数据

> ### class pyweibo.weibo
一些常用基础功能API

## Settings
未来添加自定义设置支持
