from bs4 import BeautifulSoup as soup
import re
from models import Cena, Linkovi, Proizvod, Prodavnica, MyEncoder
import json

product_name = ''
price = ''
seler = ''

cene = dict() 
linkovi = dict() 
prodavnica = Prodavnica()

with open('page.html', 'r') as page:
    parser = soup(page, 'html.parser')
    for item in parser.find_all('script'):
        name_list = re.search(r'var product_name = "(.*)";', str(item)) 
        if name_list:
            product_name = name_list.group(1)
            break

    for item in parser.find_all('tr'):
        price = re.search(r'data-price="([0-9]*\.[0-9]*)" ', str(item))
        seller = re.search(r'data-seller="([-a-zA-Z1-9]*)"', str(item))
        seller_id = re.search(r'data-sellerid="([0-9]*)"', str(item))
        store_link = re.search(r'href="([^"]*)"', str(item))
        item_pos = re.search(r'data-position="([0-9]*)"', str(item))
        
        cena = Cena(0, -1, 0, 0)
        link = Linkovi(0, "")

        if price:
            #print(price.group(1))
            cena.cena = price.group(1)

        if seller:
            #print(seller.group(1))
            prodavnica.ime = seller.group(1)

        if seller_id:
            #print(seller_id.group(1))        
            prodavnica.id = seller_id.group(1)
            link.id_prod = seller_id.group(1)
            cena.id_prod = seller_id.group(1)
        
        if store_link:
            #print(store_link.group(1).replace('amp;', ''))
            link.link = store_link.group(1).replace('amp;', '')
        
        if item_pos:
            #print(item_pos.group(1))
            cena.id = item_pos.group(1)
        if cena.id != -1:
            if cena.id not in cene.keys():
                cene[cena.id] = cena
            if link.id_prod not in linkovi.keys():
                linkovi[link.id_prod] = link


encoder = MyEncoder()
proizvod = Proizvod(product_name, 0, {}, {})
proizvod.cene = cene
proizvod.linkovi = linkovi
#proizvod.print()
#print(encoder.encode(cene))
print(encoder.encode(proizvod))