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
		self._connect_mysql(db_config)

	def _connect_mysql(self, db_config):
		log.info("Connect mysql.....")
		if db_config is None:
			log.error("No mysql config.......")

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
			log.error("error:{}.....".format(e))
			result = list()
		return result

	def excute_mysql(self, sql_str):
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

	def close_connection(self):
		"""
		waring: it's necessary
		:return:
		"""
		self.connection.close()

