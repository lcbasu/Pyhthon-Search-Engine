def lookup(index,keyword):
	for e in index:
		if e[0] == keyword:
			return e[1]
	return []

def add_to_index(index,keyword,url):
	keyword_already_present = False
	for e in index:
		if e[0] == keyword:
			keyword_already_present = True			
			e[1].append(url)
			return
	if not keyword_already_present:
		index.append([keyword,[url]])

def add_page_to_index(index,url,contents):
	keywords = contents.split()
	for e in keywords:
		add_to_index(index,e,url)

		
index = []
url = 'fake.test'
contents = 'This is a test'
url2 = 'real.test'
contents2 = 'This is not a test'

add_page_to_index(index,url,contents)
add_page_to_index(index,url2,contents2)

print index