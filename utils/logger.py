# -*- coding: utf-8 -*-
"""
   Author :        Jesper
   Date：          2020/5/25 17:31
   Description :
   Changed by:
"""


import logging
import threading

global_data = threading.local()

log_level_case = 1
log_level_map = {
				 0: logging.DEBUG,
				 1: logging.INFO,
				 2: logging.ERROR
}
log_level= log_level_map[log_level_case]

class UuidFilter(logging.Filter):
	def filter(self, record):
		uuid = getattr(global_data, 'uuid', None)
		record.uuid = uuid
		return True

log = logging.getLogger(__name__)
handler = logging.StreamHandler()
handler.setLevel(log_level)

formatter = logging.Formatter(
	'%(asctime)s %(levelname)s %(process)d --- [%(threadName)s] %(filename)s:%(lineno)-4d: %(message)s'
)
handler.setFormatter(formatter)

log.addHandler(handler)
log.setLevel(log_level)
log.addFilter(UuidFilter())