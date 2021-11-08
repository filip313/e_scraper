from bs4 import BeautifulSoup as soup
from urllib.request import pathname2url 
import re

product_name = ''
price = ''
seler = ''
with open('page.html', 'r') as page:
    parser = soup(page, 'html.parser')
    for item in parser.find_all('script'):
        name_list = re.search(r'var product_name = "(.*)";', str(item)) 
        if name_list:
            print(name_list.group(1))
            break

    for item in parser.find_all('tr'):
        price = re.search(r'data-price="([0-9]*\.[0-9]*)" ', str(item))
        seller = re.search(r'data-seller="([-a-zA-Z1-9]*)"', str(item))
        seller_id = re.search(r'data-sellerid="([0-9]*)"', str(item))
        store_link = re.search(r'href="([^"]*)"', str(item))
        item_pos = re.search(r'data-position="([0-9]*)"', str(item))

        if price:
            print(price.group(1))

        if seller:
            print(seller.group(1))

        if seller_id:
            print(seller_id.group(1))        
        
        if store_link:
            print(store_link.group(1).replace('amp;', ''))
        
        if item_pos:
            print(item_pos.group(1))

        print()

print(product_name)