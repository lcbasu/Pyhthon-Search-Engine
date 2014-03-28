page = '<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8" /><meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1"><title>iFest 2012</title><link rel="stylesheet" type="text/css" href="css/style_makeover.css" /><p class="copyright"><span>&copy; IEEE IIT Roorkee | <a href="http://ifest.ieeeiitr.com/ifest_2011.php">iFest 2011</a></span></div></body></html>'

start_link = page.find('<a href="')
start_quote = page.find('"',start_link)
end_quote = page.find('"', start_quote+1)
url = page[start_quote+1:end_quote]
print url
