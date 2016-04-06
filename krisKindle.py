import random
import getpass

def buildMail(mailTo, mailFrom, recipientName, name):
	header = 'To:' + mailTo + '\n' + 'From:' + mailFrom + '\n' + 'Subject: Kris Kindle\n\n'
	message = 'Dear ' + recipientName + ',\n\n'
	message = message + 'You have drawn ' + name + ' in the Kris Kindle draw!\n\n'
	message = message + 'Not sure when we\'ll be exchanging these gifts but there\'s a limit of 10 euro.\n\n'
	message = message + 'Merry Christmas!\n\n'
	message = message + 'From your extrememly talented draw organiser!'
	return header + message

def sendMail(participant, name, mailFrom, password):
	import smtplib
	mailTo = participant[1]
	recipientName = participant[0]
	email = buildMail(mailTo, mailFrom, recipientName, name)
	# Send the mail
	server = smtplib.SMTP("smtp.gmail.com:587")
	server.starttls()
	server.login(mailFrom, password) # "Allow less secure apps:" will have to be switched to ON in the account settings
	server.sendmail(mailFrom, mailTo, email)
	server.quit()
	
def interactiveDraw():
	import os
	people = []
	print 'Enter the names of those taking part:'
	i = 1
	while True:
		person = raw_input('Person ' + str(i) + ':')
		if (person == '!'):
			break
		else:
			people.append(person)
			i = i + 1
	shuffledPeople = []
	for person in people:
		shuffledPeople.append(person)
	random.shuffle(shuffledPeople)
	for person in people:
		os.system('cls')
		index = (shuffledPeople.index(person)+1)%len(shuffledPeople)
		raw_input(person + ', please press enter to find out who you have drawn!')
		print 'You have drawn ' + shuffledPeople[index] + '.'
		print 'Please press enter now to prepare the screen for the next person.'
		raw_input()
	os.system('cls')

def automaticDraw(people):
	if (len(people) == 0):
		i = 1
		while True:
			person = raw_input('Name of person ' + str(i) + ':')
			if (person == '!'):
				break
			else:
				email = raw_input(person + '\'s email address:')
				people.append((person, email))
				i = i + 1
	shuffledPeople = []
	for person in people:
		shuffledPeople.append(person[0])
	random.shuffle(shuffledPeople)
	i = 1
	fromEmail = raw_input('Email to send from:')
	password = getpass.getpass('Password:')
	for person in people:
		index = (shuffledPeople.index(person[0])+1)%len(shuffledPeople)
		sendMail(person, shuffledPeople[index], fromEmail, password)
		print 'Sent email number ' + str(i)
		i = i + 1

predesignedDraw = raw_input('Predesigned draw?[y/n]')
if (predesignedDraw == 'y'):
	people = (('John','johnorr123@gmail.com'),('Harry','harrycrowe1993@gmail.com'),('Louis','koalamanana@gmail.com'),('Stephen','mcste93@gmail.com'),('Rob','r-ellis@hotmail.com'),('Rory','rory.oregan@gmail.com'),('James','james.g.stack@gmail.com'))
	automaticDraw(people)
else:
	emailMethod = raw_input('Email method?[y/n]')
	if (emailMethod == 'y'):
		automaticDraw([])
	else:
		interactiveDraw()
