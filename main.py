from menu import menu, Stor, find_profile_by_email, find_password_for_site, menu2

#menu
#1 stor
#2 find site and app conencted to an email
#3 find password for a site





passw = input("Please enter the master password for tengu: ")


if passw == "nico":
	print(' ')
	print("You are in")
	print(' ')
else:
	print("no luck")
	exit()


choice = menu()

while choice != 'Q':

	if choice == '1':
		Stor()
		choice2 = menu2()

		if choice2 == 'Q':
			choice = 'Q'
		else:
			choice = menu()


	if choice == '2':
		find_profile_by_email()
		choice2 = menu2()

		if choice2 == 'Q':
			choice = 'Q'
		else:
			choice = menu()



	if choice == '3': 
		find_password_for_site()
		choice2 = menu2()

		if choice2 == 'Q':
			choice = 'Q'
		else:
			choice = menu()


exit()

