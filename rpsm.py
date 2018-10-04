import random
a=['r','p','s']
s1=0
s2=0
while(True):
	p=input("Your Choice r/p/s: ")
	c=random.choice(a)

	print("You chose ",p,"Computer chose",c)
	if(p=='r' or p=='p'or p=="s"):
		if(p==c):
			print("tie")
		elif((p=='r' and c=='p') or(p=='p' and c=='s') or(p=='s' and c=='r')):
			s1=s1+1
			print("computer won",s1,"times")
		else:
			s2=s2+1
			print("U Won",s2,"times")
	else:
		print("Give proper input")	
		break
	if(s1==3 or s2==3):
		if(s1==3):
			print("I'M Sorry, Computer Won the game")
		else:
			print("Congrats U Won against Computer, have a great day")
		break	


		
