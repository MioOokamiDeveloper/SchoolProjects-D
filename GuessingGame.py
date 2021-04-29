import time
import os
import random
import sys

def CT():
	os.system('cls' if os.name == 'nt' else 'clear')

list = ['not here', 'nope', 'try again', 'PARADISE', 'nada', 'nein', 'again']
a = random.shuffle(list)
b = 12
print('welcome to the guessing game, here you will try to guess which room has the prize inside of it. Though you only get three trys!')
time.sleep(6)
input("press enter to continue..")
CT()
global guesses
guesses = 3
while guesses > 0:
	uInput = input('what room would you like?\n')
	uInput = int(uInput)
	if uInput > 6:
		print('list index out of range!')
		time.sleep(2)
		sys.exit()
		time.sleep(1)
		CT()
	if list[uInput] == 'not here' or list[uInput] == 'nope' or list[uInput] == 'try again' or list[uInput] == 'nada' or list[uInput] == 'nein' or list[uInput] == 'again':
		print('not there')
		time.sleep(1)
		guesses -= 1
		if guesses == 1:
			print('1 try left')
			time.sleep(2)
			CT()
		else:
			print(str(guesses) + ' trys left!')
			time.sleep(2)
			CT()
	if list[uInput] == 'PARADISE':
		print('congradulations! you won a trip to hawaii\n')
		b += 1
	if guesses <= 0:
		uInput = input('good game, try again?\n')
		if uInput == 'yes' or 'y':
			print('running it back!')
			time.sleep(2)
			b = 12
			guesses = 3
			CT()
		elif uInput == 'no' or 'n':
			print('come again soon!')
			time.sleep(2)
			CT()
			sys.exit()
