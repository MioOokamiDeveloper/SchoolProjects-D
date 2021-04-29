import os
import random
import time
def CT():
	os.system('cls' if os.name == 'nt' else 'clear')

a = 12
while a == 12:
	print('enter your question')
	uinput = input()
	b = random.choice(['yes', 'no', 'maybe', 'ask again later', 'outlook is good', 'outlook is not good', 'most likely no', 'most likely yes'])
	print(b)
	time.sleep(2)
	CT()
