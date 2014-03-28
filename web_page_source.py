import urllib

def get_web_page(url):
	response = urllib.urlopen(url)
	page_source = response.read()
	return page_source

url1 = "http://www.facebook.com"
url2 = "http://www.google.com"
list = [get_web_page(url1),get_web_page(url2)]
print list