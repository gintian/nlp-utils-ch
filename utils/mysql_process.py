# -*- coding: utf-8 -*-
"""
   Author :        Jesper
   Date：          2020/5/25 17:30
   Description :
   Changed by:
"""

import pymysql.cursors
import pymysql
from utils.logger import log


class mysqlProcess():
	def __init__(self, db_config=None):
		self.connect_mysql(db_config)

	def connect_mysql(self, db_config):
		log.info("Connect mysql.....")
		if db_config is None:
			db_config = {
				# "host": "rm-uf6s683d4lm7bh74swo.mysql.rds.aliyuncs.com",  # 外网地址
				"host": "rm-uf6s683d4lm7bh74s.mysql.rds.aliyuncs.com",  # 内网地址
				"user": "plat_data_popinion",
				"password": "CqUo3ewA5F6lRP5V",
				"database": "popinion",
				"port": 3306,
				"charset": "utf8",

				# "autocommit":True
			}

		mysql_host = db_config["host"]
		mysql_user = db_config["user"]
		mysql_password = db_config["password"]
		mysql_db = db_config["database"]
		try:
			log.info("Connect mysql..., database:{}, host:{}".format(mysql_db, mysql_host))
			self.connection = pymysql.connect(host=mysql_host,
			                                  user=mysql_user,
			                                  password=mysql_password,
			                                  db=mysql_db,
			                                  charset='utf8',
			                                  cursorclass=pymysql.cursors.DictCursor)
			log.info("Connect mysql sucess....")
		except Exception as e:
			log.error("error.....")

	def insert_data(self, sql_str):
		try:
			with self.connection.cursor() as cursor:
				# Create a new record
				cursor.execute(sql_str)

			# connection is not autocommit by default. So you must commit to save
			# your changes.
			self.connection.commit()
		except Exception as e:
			print('Error e:{}'.format(e))
			self.connection.rollback()

	def insert_many(self, sql_str, val):
		try:
			# 执行sql语句
			with self.connection.cursor() as cursor:
				cursor.executemany(sql_str, val)
			# 提交到数据库执行
			self.connection.commit()
		except Exception as e:
			# 如果发生错误则回滚
			print('Error e:{}'.format(e))
			self.connection.rollback()

	def query_data(self, sql_str):
		try:

			with self.connection.cursor() as cursor:
				# Read a single record
				cursor.execute(sql_str)
				result = cursor.fetchall()

		except Exception as e:
			print('Error e:{}'.format(e))
			result = list()
		return result

	def close_connection(self):
		"""
		waring: it's necessary
		:return:
		"""
		self.connection.close()

