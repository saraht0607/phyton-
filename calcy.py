i=int(input("enter value of a:"))
j=int(input("enter value of b:"))
o=input("what do you want to do?+,-,*,/:")

def add():
	return i+j
def sub(a,b):
	return a-b
def mul(a,b):
	return a*b
def divide(a,b):
	return a/b

if(o=='+'):
	res=add()

elif(o=='-'):
	res=sub(i,j)

elif(o=='*'):
	res=mul(i,j)

elif(o=='/'):
	res=divide(i,j)

print(res)	




