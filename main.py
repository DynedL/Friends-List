import names
import random
friendsList = {
	#"Name": ["Birthday", "Phone Number", "Email"]
}
emailList = [
  "@yahoo.com", "@gmail.com", "@email.com", "@hotmail.com", "@outlook.com", "@icloud.com", "aol.com",
	]

randomIndex = random.randint(0,len(emailList)-1) 
wordFromBank = emailList[randomIndex]
def addFriend():
	print()
	name = input("Please enter your friends name: ")
	bday = 'Birthday:' + input("Please enter your friends birthday: ")
	number = 'Phone Number:' + input("Please enter your friends phone number: ")
	email = 'Email:' + input("Please enter your friends email: ")

	friendsList[name] = [bday, number, email]
	input("Press enter to continue")
	#print(friendsList)

def deleteFriends():
	print()
	num = (len(friendsList))
	if num > 0:
		print("There are currently", num, 'friend(s) in your friends list')
		allFriends = friendsList.keys()
		for eachFriend in allFriends:
			print("			", eachFriend)
		print("Whose info would you like to delete?")
		friend = input()
		try: 
			print()
			friendsList.pop(friend)
			print(friend+"'s info has been deleted.")
		except: 
			print()
			print("Unknown Friend")
			input("Press enter to continue")
	else: 
		print("Try making some new friends")
	input("Press enter to continue")

def editFriend():
	print()
	num = (len(friendsList))
	print("There are currently" , num , "friend(s) in your list")
	if num > 0:
		allFriends = friendsList.keys()
		for eachFriend in allFriends:
			print("    " , eachFriend)
		print("Whose info would you like to edit?")
		friend = input()
		try:
			oldinfo = friendsList.pop(friend)
			change = 0
			print('enter your friends name, or press enter for original value: ')
			name = input()
			if name == '':
				name = friend
				change += 1
			print('enter your friends birthday, or press enter for original value: ')
			bday = 'Birthday: ' + input()
			if bday == 'Birthday: ':
				bday = oldinfo[0]
				change += 1
			print('enter your friends phone number, or press enter for original value: ')
			number = 'Phone Number: ' + input()
			if number == 'Phone Number: ':
				number = oldinfo[1]
				change += 1
			print('enter your friends Email, or press enter for original value: ')
			email = 'Email: ' + input()
			if email == 'Email: ':
				email = oldinfo[2]
				change += 1
			friendsList[name] = [bday, number, email]
			if change == 4:
				print("You didn't change any of " + name+"'s info")
				input("press enter to continue")
			else:
				print(name+"\'s info has been changed in your friend list!")
				input("press enter to continue")
		except:
			print("that friend is not in your list, or you mistyped their name")
			input("press enter to continue")
	else:
		print("try again after making a few friends.")
		input("press enter to continue")

def showFriends(): 
	print()
	num = (len(friendsList))
	if num > 0:
		print("There are currently", num, 'friend(s) in your friends list')
		allFriends = friendsList.keys()
		for eachFriend in allFriends:
			print("			", eachFriend)
		print("Whose info would you like to see?")
		friend = input()
		try:
			info = friendsList[friend]
			print()
			print("info on", friend)
			for item in info:
				print()
				print(item)
		except: 
			print()
			print("Unknown Friend")
			input("press enter to continue")
	else: 
		print("Try making some new friends")
	input("Press enter to continue")

def findAFriend():
	fname = names.get_first_name()
	lname = names.get_last_name()
	emailNames = [
	fname+"."+lname, fname+"_"+lname, lname+"."+fname, lname+"_"+fname, fname+"_", lname+"_", lname+"-", lname+".", fname+"-", fname+".", fname+lname, lname+fname, "Xx_"+fname+"_xX", "Xx_"+lname+"_xX", fname, lname, 
]
	randomIndex = random.randint(0,len(emailList)-1) 
	emailweb = emailList[randomIndex]
	RandomIndex = random.randint(0,len(emailNames)-1)
	emailname = emailNames[RandomIndex]

	fullname=fname+" "+lname
	bday ='Birthday: ' + str(random.randrange(1,12))+"/"+str(random.randrange(1,28))
	number ='Phone Number: ' + str(random.randrange(100,999))+"-"+str(random.randrange(100,999))+"-"+str(random.randrange(1000,9999))
	email ='Email: ' + emailname+str(random.randrange(100,999))+emailweb
	friendsList[fullname] = [bday, number, email]
	



	print(fullname, "has been added to your friend list!")
	input("press enter to continue")



Run = True
while Run:
	print()
	print()
	print("Commands:")
	print("1. Add a friend")
	print("2. Delete a friend")
	print("3. Edit a friend")
	print("4. View a friend")
	print("5. Find a friend")
	print("6. Exit")
	print()
	print("What command would you like to execute (1-6)? ")
	choice = input()

	if choice == '1':
		addFriend()
	if choice == '2':
		deleteFriends()
	if choice == '3':
		editFriend()
	if choice == '4':
		showFriends()
	if choice == '5':
		findAFriend()
	if choice == '6':
		Run = False

print("Thank you for using friends list.")
