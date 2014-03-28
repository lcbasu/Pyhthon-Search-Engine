import urllib

def get_web_page(page_url):
	response = urllib.urlopen(page_url)
	page_source = response.read()
	return page_source

def bad_hash_string(keyword,buckets):
	return ord(keyword[0])%buckets

	
def hash_string(keyword, buckets):
	word_value = 0
	for e in keyword:
		word_value = (word_value + ord(e))%buckets
	return word_value
	
def test_hash_function(func,keys,size):
	results = [0]*size
	keys_used = []
	for w in keys:
		if w not in keys_used:
			hv = func(w,size)
			results[hv] += 1
			keys_used.append(w)
	return results

words = get_web_page('http://www.techcrunch.com').split()
print len(words),'\n'

print test_hash_function(bad_hash_string,words,100)
print '\n'
print test_hash_function(hash_string,words,100)