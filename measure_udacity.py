def measure_udacity(p):
	letters_with_u = 0
	for e in p:
		if e[0] == 'U':
			letters_with_u = letters_with_u +1
	return letters_with_u
	
list1 = ['Sam','Liyo','Jim']
list2 = ['Sohan','Rayan','Sachdeva','Urwashi']
list3 = ['Ukrain','Utarrakhand','Utapia']
	
print 'list1'
print str(measure_udacity(list1)) + '\n'
print 'list2'
print str(measure_udacity(list2)) + '\n'
print 'list3'
print measure_udacity(list3)
