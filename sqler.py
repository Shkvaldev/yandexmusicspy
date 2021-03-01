import sqlite3

from telebot import types

class Sqler:
	def __init__(self, database):
		self.conn = sqlite3.connect(database,check_same_thread = False)
		self.cursor = self.conn.cursor()

	def register(self, user):
		with self.conn:
			self.cursor.execute("SELECT * FROM telegram WHERE user_id = '{}'".format(user[1]))
			new = self.cursor.fetchone()
			if new == None:
				self.cursor.execute("INSERT INTO telegram VALUES(?,?,?,?,?,?);", user)
				return "Вы успешно зарегистрированы!"
			else:
				return "С возвращением 😉"

	def get_status(self, user_id):
		with self.conn:
			user =  self.cursor.execute("SELECT * FROM telegram WHERE user_id = '{}'".format(user_id))
			status = user.fetchall()
			result = status[0][2]
			return result

	def get_balance(self, user_id):
		with self.conn:
			user =  self.cursor.execute("SELECT * FROM telegram WHERE user_id = '{}'".format(user_id))
			status = user.fetchall()
			result = status[0][3]
			return result

	def add_subscribe(self, subscribe):
		with self.conn:
			self.cursor.execute("UPDATE telegram SET balance = (balance - 250) WHERE user_id = '{}'".format(subscribe[0]))
			self.cursor.execute("UPDATE telegram SET status = 'sub' WHERE user_id = '{}'".format(subscribe[0]))
			self.cursor.execute("UPDATE telegram SET sub_time = '{}' WHERE user_id = '{}'".format(subscribe[1], subscribe[0]))
