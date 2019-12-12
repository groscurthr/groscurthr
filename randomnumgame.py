#test

import random

number = random.randrange(1,11) 


print("Guess the number. You'll get 5 tries.\nEnter a number from 1-10: ")

usernum = int(input())

count = 0
while count<4:
	if number != usernum:
		print('not correct, try again')
		usernum = int(input())
		count += 1
	elif number == usernum:
		print('correct')
		break
else:
	print('out of tries, number was', number)
