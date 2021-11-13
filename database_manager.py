import psycopg2
from hash_maker import decrypte_password

#store the information in database
def store_informlation(username, password, email, site, url):
	try:
		connection = connect()
		cur = connection.cursor()

		postgres_insert_query = """INSERT INTO data (username, password, email, site, url) VALUES (%s ,%s ,%s ,%s ,%s)"""
		record_to_insert = (username, password, email, site, url)

		cur.execute(postgres_insert_query, record_to_insert)
		connection.commit()

	except (Exception, psycopg2.Error) as error:
		print(error)

#get inforamtion for an email 
def get_information_from_email(email):
	try:
		connection = connect()
		cur = connection.cursor()

		postgres_insert_query = """SELECT * FROM data WHERE email= '""" + email + "'" 
		cur.execute(postgres_insert_query) 
		connection.commit()

		result = cur.fetchall()
		data = ["username", "password", "email", "site", "url"]

		for row in result:
			for i in range(0, len(row)):
				if i == 1:

					password = row[i]
					password1 = password[1: len(row[i])] 
					password2 = bytes(password1, 'utf-8')

					realpassword = decrypte_password(password2)
					realpassword1 = str(realpassword)
					realpassword2 = realpassword1[2 : (len(realpassword1)-1)]

					print(" ")
					print("Password: ", realpassword2)
					print("---"*30)

				else:
					print(" ")
					print(data[i] + ": " +row[i])
					print("---"* 30)

	except (Exception, psycopg2.Error) as error:
		print(error)


#get password for a site
def get_password_from_site(site):
	try:
		connection = connect()
		cur = connection.cursor()

		postgres_insert_query = """SELECT password FROM data WHERE site= '""" + site + "'" 
		cur.execute(postgres_insert_query) 
		connection.commit()

		result = cur.fetchall()

		for row in result:
			for i in range(0, len(row)):
				password_crypt = row[i]
				return password_crypt
		
	except (Exception, psycopg2.Error) as error:
		print(error)


#get all inforamation for a site
def get_inforamtion_from_site(site):
	try:
		connection = connect()
		cur = connection.cursor()

		postgres_insert_query = """SELECT * FROM data WHERE site= '""" + site + "'" 
		cur.execute(postgres_insert_query) 
		connection.commit()

		result = cur.fetchall()
		data = ["username", "password", "email", "site", "url"]	

		print("Result for information for {}: ".format(site))
		print("---"* 30)

		for row in result:
			for i in range(0, len(row)):
				print(data[i] + ": " +row[i])
				print("---"* 30)
				
		
	except (Exception, psycopg2.Error) as error:
		print(error)


#for get connected to database
def connect():
	try:

		connection = psycopg2.connect(user="postgres", password="nico", host="127.0.0.1", database="Password_manager")
		return connection

	except :
		print("you are not connect on database")




