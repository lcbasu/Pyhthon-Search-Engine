def lookup(index,keyword):
	for e in index:
		if e[0] == keyword:
			return e[1]
	return []

index = [['free_learning',['http://www.google.com/']],['udacity',['http://www.google.com/','http://www.udacity.com/']]]
keyword = 'udacity'

print lookup(index,keyword)