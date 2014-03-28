print 'Using iteration\n'

def factorial(n):
	if n==0:
		return 1
	i = 1
	while n!=1:
		i = i*n
		n = n-1
	return i

print factorial(2)



print 'Using recursion\n'

def factorial_recursion(n):
	if n==0:
		return 1
	if n==1:
		return n
	return n*factorial(n-1)

print factorial_recursion(2)