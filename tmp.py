#!user/bin/python
# _*_ coding: utf-8 _*_
# @Author      :   Jesper
# @Time        :   2020/9/8 18:45
# @Description :

from nlp_utils_ch.utils.logger import log

log.info("Begin.....")
result = list()
for i in range(3000):
	result.append(i)

log.info("End.....")