import search, buttons, time, registerUser, registerAuthorizer

search = search.Search()
but = buttons.Buttons()
count = 0


def sButPressed(title):

	if title == "Register User":
		regUser = registerUser.RegisterUser()
		regUser.main()
	elif title == "Register Authorizer":
		regAutho = registerAuthorizer.RegisterAuthorizer()
		regAutho.main()


def mButPressed():
	global count
	count+=1

	if count == 1:
		print("Register User")
		timestamp1 = time.time()
		while (time.time()-timestamp1) <= 120:
			if but.button_2():
				sButPressed("Register User")
			elif but.button_1():
				count+=1
				break
	elif count == 2:
		print("Register Authorizer")
		timestamp1 = time.time()
		while (time.time()-timestamp1) <= 120:
			if but.button_2():
				sButPressed("Register Authorizer")
			elif but.button_1():
				count+=1
				break

	else:
		print("Put Finger")
		count = 0


while True:
	if but.button_1():
		mButPressed()
	else:
		print("Put Finger")
		search.main()

	time.sleep(1)
