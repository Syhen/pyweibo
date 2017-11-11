# -*- coding: utf-8 -*-
"""
create on 2017-11-05 下午5:19

author @heyao
"""

import logging


def get_logger(name, log_level="INFO", format_str=None):
    format_str = format_str or "[%(name)s] [%(levelname)s] %(message)s"
    logging.basicConfig(format=format_str)
    logger = logging.getLogger(name)
    logger.setLevel(getattr(logging, log_level))
    logger = logging.LoggerAdapter(logger, extra={})
    return logger
