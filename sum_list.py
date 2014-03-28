def sum_list(p):
	sum = 0
	for e in p:
		sum = sum + e
	return sum

list1 = [1,2,3]
list2 = [1,2,3,4,5]

print 'Sum of list1'
print str(sum_list(list1)) + '\n'
print 'Sum of list2'
print sum_list(list2)