#!user/bin/python
# _*_ coding: utf-8 _*_
# @Author      :   Jesper
# @Time        :   2020/9/16 11:56
# @Description :
import time
import datetime

def timestamp_to_local_time(time_stamp, mode="ms"):
	""":
	mode: ms/s
	"""
	if mode=="ms":
		time_local = time.localtime(time_stamp / 1000)
	else:
		time_local = time.localtime(time_stamp )
	dt = time.strftime("%Y-%m-%d %H:%M:%S", time_local)
	return dt


def to_timestamp(inpput_time):
	d = datetime.datetime.strptime(str(inpput_time), "%Y-%m-%d %H:%M:%S")
	t = d.timetuple()
	time_stamp = int(time.mktime(t))
	return time_stamp