from database_manager import *
from hash_maker import *
from termcolor import colored

def menu():
	"""
	print('--'*38)
	print('-'*30 + "Password manager" + '-'*30)
	print('--'*38)
	"""
	ascii_art = (r""" 
 _____                                    _ 
|  __ \                                  | |
| |__) |_ _ ___ _____      _____  _ __ __| |
|  ___/ _` / __/ __\ \ /\ / / _ \| '__/ _` |
| |  | (_| \__ \__ \\ V  V / (_) | | | (_| |
|_|   \__,_|___/___/ \_/\_/ \___/|_|  \__,_|
""")

	print(colored(ascii_art, 'green'))




	print(" ")
	print(" 1. Store a new password")
	print(" 2. Find all site and app connected to an email")
	print(" 3. Find password for a site or app")
	print(" Q. Exit")
	print('--'*38)
	return input(": ")

def Stor():#fini focntionelle
	print("Please enter the site:")
	site = input()
	print("Please enter url of site:")
	url = input()
	print("Please enter your username:")
	username = input()
	print("Please enter your email:")
	email = input()
	print("Please enter your password:")
	password = input()
	password_encrypt = encrypte_password(password)

	store_informlation(username, str(password_encrypt), email, site, url)


def find_password_for_site():#encour :)
	print("Please enter the site: ")
	site = input()

	password = get_password_from_site(site)#value str with the b for bytes
	password1 = password[1: len(password)]#delet this b / probleme est que password est en string mais avec le b bytes
	password2 = bytes(password1, 'utf-8')#convert to bytes for decrypt

	real_password = decrypte_password(password2)
	real_password1 = str(real_password)
	real_password2 = real_password1[2 : (len(real_password1)-1)]
	print("Your password is: " + real_password2)

	


def find_profile_by_email():
	print("Enter your email")
	email = input()

	get_information_from_email(email)


def menu2():
	print(" ")
	print("1: for return to menu")
	print("Q: for quit")
	return input(": ")

		