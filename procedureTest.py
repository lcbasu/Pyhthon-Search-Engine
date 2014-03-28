def rest_of_string(s):
	return s[1:]

print rest_of_string('audacity')

def sum(a,b):
	print 'a is',a
	a=a+b
	print 'a is',a
	print 'exit without return statement, so the result is :'

print sum(1,2)

def sumModified(a,b):
	a=a+b
	return a

print sumModified('hello','lokesh')