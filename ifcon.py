# if conditions
x=int(input("enter a number:"))
if(x%2==0):
	print(x,"is an even number")
elif(x%2!=0):
	print(x,"is an odd number")
elif(x>0):
	print(x,"is a positive number")
elif(x==0):
	print(x,"is zero")
elif(x<0):
	print(x,"is a negative number")

elif(x>y):
	print(x,"is greater than",y)

else:
	print(y,"is greater than",x)