import random



while True:
	i=input("enter 'r' to roll 'p' quit")
	if(i=='r'):
		print("Bye!")
		exit()
	elif(i=='p'):
		print("You got",random.randint(1,6))
	else:
		print("press r to roll")

