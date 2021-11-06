from urllib import request

def ucitaj_linkove(putanja):
	with open(putanja, 'rt') as f:
		linkovi = []
		for line in f:
			linkovi.append(line.strip())

		return linkovi
   
 
def preuzmi_sajt(link):
	with request.urlopen(link) as page:
		decoded_page = ''
		for line in page:
			line = line.decode('utf-8')
			decoded_page += line

		return decoded_page	


putanja_do_linkova = "./linkovi.txt"
linkovi = ucitaj_linkove(putanja_do_linkova)
for link in linkovi:
	page = preuzmi_sajt(link)
	with open('page.html', 'w') as f:
		f.write(page)
