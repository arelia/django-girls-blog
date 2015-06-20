print("Hello, Django Girls!")

myInfo = {'firstName': 'Arelia', 'lastName': 'Jones'}

print("My name is " + myInfo['firstName'] + " " + myInfo['lastName'] + ".")

a = 4
b = 6

if a == 4:
	print(" is greater than ")

elif b == 2:
	print(" is less than ")
else:
	print("I don't know the answer")

def hi():
	print('Hi there!')
	print('How are you?')

hi()


def hi(name):
	if name == "Arelia":
		print("Hi Arelia!")
	elif name == "Jones":
		print("Hi Jones!")
	else:
		print("Hi anonymous!")

hi("Ola")

def hi(name):
	print("Hi " + name + "!")

hi("Rachel")