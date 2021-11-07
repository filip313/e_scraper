from bs4 import BeautifulSoup as soup
import re

product_name = ''
with open('page.html', 'r') as page:
    parser = soup(page, 'html.parser')
    for item in parser.find_all('script'):
        name_list = re.findall(r'\bvar product_name = "(.*)";', str(item)) 
        if name_list != []:
            product_name = name_list.pop()
            break
    
    for item in parser.find_all('tr'):
        print(item)
        print()

print(product_name)