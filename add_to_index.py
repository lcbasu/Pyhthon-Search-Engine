def add_to_index(index,keyword,url):
	keyword_already_present = False
	for e in index:
		if e[0] == keyword:
			keyword_already_present = True
			if url not in e[1]:
				e[1].append(url)
				return
	if not keyword_already_present:
		index.append([keyword,[url]])
		
		
index = [['free_learning',['http://www.google.com/']],['udacity',['http://www.google.com/','http://www.udacity.com/']]]
keyword = 'random'
url = 'http://www.asd.com/'

add_to_index(index,keyword,url)

print index