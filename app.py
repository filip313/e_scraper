from urllib import request
from bs4 import BeautifulSoup as soup
import re
from models import Cena, Linkovi, Proizvod, Prodavnica, MyEncoder
from datetime import datetime

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

def parsiraj_podatke(page):
	
	product_name = ''
	price = ''
	seler = ''
	cene = dict() 
	linkovi = dict() 
	prodavnice = dict()
	parser = soup(page, 'html.parser')

	for item in parser.find_all('script'):
		name_list = re.search(r'var product_name = "(.*)";', str(item)) 
		if name_list:
			product_name = name_list.group(1)
			break

	for item in parser.find_all('tr'):
		price = re.search(r'data-price="([0-9]*\.[0-9]*)" ', str(item))
		seller = re.search(r'data-seller="([-a-zA-Z1-9 ]*)"', str(item))
		seller_id = re.search(r'data-sellerid="([0-9]*)"', str(item))
		store_link = re.search(r'href="([^"]*)"', str(item))
		item_pos = re.search(r'data-position="([0-9]*)"', str(item))
        
		cena = Cena(0, -1, 0, 0)
		link = Linkovi(0, "")
		prodavnica = Prodavnica()
		if price:
            #print(price.group(1))
			cena.cena = price.group(1)

		if seller:
            #print(seller.group(1))
			prodavnica.ime = seller.group(1)

		if seller_id:
            #print(seller_id.group(1))        
			prodavnica.id = seller_id.group(1)
			prodavnice[prodavnica.id] = prodavnica
			link.id_prod = seller_id.group(1)
			cena.id_prod = seller_id.group(1)
        
		if store_link:
            #print(store_link.group(1).replace('amp;', ''))
			link.link = "https://www.eponuda.com" + store_link.group(1).replace('amp;', '')
        
		if item_pos:
            #print(item_pos.group(1))
			cena.id = len(cene.keys()) + 1
			cena.datum = str(datetime.now().date())

		flag = True 
		if cena.id != -1:
			for c in cene.values():
				if c.id_prod == cena.id_prod and c.datum == cena.datum:
					flag = False
					break
			if flag:
				cene[cena.id] = cena
			if link.id_prod not in linkovi.keys():
				linkovi[link.id_prod] = link

	proizvod = Proizvod(product_name, -1, cene, linkovi)

	return prodavnice, proizvod

def ispis(prodavnice, proizvodi):
	for proizvod in proizvodi.values():
		print(proizvod.ime)
		print('----------------------------------------------')
		prod_ids = []
		for cena in proizvod.cene.values():
			if cena.id_prod not in prod_ids:
				prod_ids.append(cena.id_prod)

		for prod_id in prod_ids:
			print(f'\t{prodavnice[prod_id].ime}')
			print(f'\t{proizvod.linkovi[prod_id].link}')
			print(f'\t\tDATUM      | CENA')
			for cena in proizvod.cene.values():
				if cena.id_prod == prod_id:
					print(f'\t\t{cena.datum} | {cena.cena}')
					print('\t\t========================')
		
		print('\n')

def save_data(proizvodi, prodavnice):
	encoder = MyEncoder()	
	
	with open("proizvodi.json", 'w') as f:
		f.write(encoder.encode(proizvodi))

	with open("prodavnice.json", 'w') as f:
		f.write(encoder.encode(prodavnice))

putanja_do_linkova = "./linkovi.txt"
linkovi = ucitaj_linkove(putanja_do_linkova)
proizvodi = dict()
prodavnice = dict()
for link in linkovi:
	page = preuzmi_sajt(link)
	prod, proi = parsiraj_podatke(page)
	proi.id = len(proizvodi.keys()) + 1
	proizvodi[proi.id] = proi
	prodavnice.update(prod)

encoder = MyEncoder()
#print(encoder.encode(prodavnice))
ispis(prodavnice, proizvodi)
save_data(proizvodi, prodavnice)