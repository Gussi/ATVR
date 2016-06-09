from  productscraper import request
from bs4 import BeautifulSoup
import requests
import re

#Some observations: the product ID is always a zero-padded 5 digit number
base_url = "http://www.vinbudin.is/Heim/v%C3%B6rur/stoek-vara.aspx/?productid="

valid_products = []
valid = 0


#Bruteforce the entire product range because fuck messing with dynamic content!
for i in range(0, 100000, 10):
    urls = []
    for n in range(10):
        #10 async HTTP requests seems to be the fastest I can get this
        #This results in about 2 - 3 responses per second. Slow!
        urls.append(base_url + str(i + 5).zfill(5))
    products = request(urls)
    valid += len(products)
    valid_products += products
    #TODO: do something with valid products
    #Database maybe?
    #json blob?
    print("Scraped: {}\nValid: {}\n\n".format(i + 1, valid))
    
