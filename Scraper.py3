from bs4 import BeautifulSoup
from urllib.request import urlopen, urlretrieve
from time import sleep

links = []
mainUrl = "http://http.developer.nvidia.com/GPUGems3/"

f = open('output.html', 'w')
f.write("""<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>GPU Gems 3</title>
  </head>
  <body>""")

def openPage():
	startUrl = "gpugems3_pref01.html"
	content = urlopen(mainUrl + startUrl)
	soup = BeautifulSoup(content, 'html.parser')

	links_text = soup.find(id="right").find_all("a")
	
	for link in links_text:
		links.append(link.get("href"))

	return soup

def scrapeImages(imgs):
	for img in imgs:
		name = img.get("src")
		print("[IMG]: Parsing image " + name)
		urlretrieve(mainUrl + name, name)

def parsePage(url):
	print("[HTLM]: Parsing " + url)

	content = urlopen(mainUrl + url)
	soup = BeautifulSoup(content, 'html.parser')

	body = soup.find(id="center")
	f.write(str(body.hr))

	images = body.hr.find_all("img")
	scrapeImages(images)
	print("\n")


soup = openPage()

for url in links:
	parsePage(url)
	sleep(2)

# parsePage("gpugems3_ch01.html")

f.write("""  </body>
</html>
""")

f.close()