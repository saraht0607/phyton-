
	if(p in a):
		if(a[int(p)-1]=='X' or a[int(p)-1]=='O'):a=['1','2','3','4','5','6','7','8','9']

def print_Board():
	print(a[0],'|',a[1],'|',a[2])
	print("----------")
	print(a[3],'|',a[4],'|',a[5])
	print("----------")
	print(a[6],'|',a[7],'|',a[8])

playerOneTurn=True
while True:
	print_Board()
	p=input("Choose an available place : ")

			print("Place taken, choose another place...")
			continue
		else:
			if playerOneTurn:
				print("Player 1 >>")
				a[int(p)-1] ='X'
				playerOneTurn = not playerOneTurn
			else:
				print("Player 2 >>")
				a[int(p)-1] ='O'
				playerOneTurn = not playerOneTurn
			for i in(0,3,6):
				if(a[i]==a[i+1] and a[i]==a[i+2]):
					print("Game Over");
					exit()
			for i in range(3):
				if(a[i]==a[i+3] and a[i]==a[i+6]):
					print("Game Over...")
					exit()
#checking for diagonal(from left to right)
	if(a[0]==a[4] and a[0]==a[8]):
		print("game over")
		if(a[4]=='X'):
			print("congratulations to Player 1")
		else:
			print("congratulations to Player 2")
		printBoard()
		exit()
#checking for diagonal (from right to left)
	if(a[2]==a[4] and a[2]==a[6]):
		print("game over")
		if(a[4]=='X'):
			print("congratulations to player 1")	
		else:
			print("congratulations to player 2")
		printBoard()
		exit()
	else:
		print("You have entered an invalid position")
		continue	



				
		
					

	

