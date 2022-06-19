import pymysql.cursors
from configparser import ConfigParser

#Database Configuration
configur = ConfigParser()
configur.read('utilities/config.ini')

sqlhost = configur.get('sqlsettings', 'hostname')
sqlusername = configur.get('sqlsettings', 'username')
sqlpassword = configur.get('sqlsettings', 'password')
sqldatabase = configur.get('sqlsettings', 'database')

#SQL Class
class SQL():
	#Initialize our database
	def __init__(self):
		self.connection = pymysql.connect(host=sqlhost, user=sqlusername, password=sqlpassword, database=sqldatabase, cursorclass=pymysql.cursors.DictCursor)

	#Get site settings
	def Settings(self):
		with self.connection:
			with self.connection.cursor() as cursor:
				sql = f"SELECT * FROM settings"
				cursor.execute(sql)
				result = cursor.fetchone()
		return result
