# regex_soup.py

import re
from urllib.request import urlopen

url = "https://www.waheediqbal.info/courses"
page = urlopen(url)
html = page.read().decode("utf-8")

pattern = "<title.*?>.*?</title.*?>"
match_results = re.search(pattern, html, re.IGNORECASE)
title = match_results.group()
title = re.sub("<.*?>", "", title) # Remove HTML tags

print(title)
<<<<<<< HEAD
sourceFile=open('scrapping.txt','w')
print(title,file=sourceFile)
sourceFile.close()
=======
print ("This is an updation by user mirat ul amina")
>>>>>>> refs/remotes/origin/main
