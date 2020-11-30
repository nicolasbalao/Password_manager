from cryptography.fernet import Fernet

"""
file = open('key.key', 'wb')

key = Fernet.generate_key()

file.write(key)
file.close()
"""

file = open('key.key', 'r')
key = file.read()


def encrypte_password(password):

	pass_word  = str(password).encode()

	f = Fernet(key)

	password_encrypte  = f.encrypt(pass_word)
	return password_encrypte



def decrypte_password(password_from_database):
	
	password_to_encrypte = password_from_database

	f = Fernet(key)

	decrypte_password = f.decrypt(password_to_encrypte)
	return decrypte_password
 	





