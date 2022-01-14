from bs4 import BeautifulSoup as soup
import re
from models import Cena, Linkovi, Proizvod, Prodavnica, MyEncoder
from datetime import datetime

product_name = ''
price = ''
seler = ''

cene = dict() 
linkovi = dict() 
prodavnice = dict()

with open('page.html', 'r') as page:
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


encoder = MyEncoder()
proizvod = Proizvod(product_name, 0, {}, {})
proizvod.cene = cene
proizvod.linkovi = linkovi
#proizvod.print()
#print(encoder.encode(cene))
#print(encoder.encode(proizvod))
#print(encoder.encode(prodavnice))
print(proizvod.ime)
print('----------------------------------------------')
for prodavnica in prodavnice.values():
    print(f'\t{prodavnica.ime}')
    print(f'\t{proizvod.linkovi[prodavnica.id].link}')
    print(f'\t\tDATUM      | CENA')
    for cena in proizvod.cene.values():
        if cena.id_prod == prodavnica.id:
            print(f'\t\t{cena.datum} | {cena.cena}')
            print('===================================================================')

    print('-----------------------------------------------')
        