from bs4 import BeautifulSoup
import requests
import sys
import re

def product_scrape(url):
    #TODO: refactor this shit, it doesn't have to be this long

    #The initial page request
    sourcetree = requests.get(url).text
    soup = BeautifulSoup(sourcetree, "html5lib")

    #All the relevant fields scraped
    price = soup.find("div", class_="price").text
    name = soup.find("h3", class_="title").text
    category = soup.find("span", class_="category").text
    subcategory = soup.find("span", class_="taste").text
    description = soup.find("div", class_="description").text

    abv_info = soup.find("span", string="Styrkleiki:")
    volume_info = soup.find("span", string="Eining:")
    id_info = soup.find("span", string='Vörunúmer:')

    #Thankfully the DOM makes sense, so I can just find the next sibling. Easy!
    abv = abv_info.find_next_sibling("span")
    volume = volume_info.find_next_sibling("span")
    product_id = id_info.find_next_sibling("span")
    abv = abv.text
    volume = volume.text
    product_id = product_id.text

    #Checking if the product is valid before doing anything else
    if product_id == "Engar upplýsingar":
        return -1

    #For some reason, all the fields are littered with garbage escape characters
    garbage = "\n\t"
    translator = str.maketrans("", "", garbage)

    #Time to strip them
    price = price.translate(translator)
    name = name.translate(translator)
    category = category.translate(translator)
    subcategory = subcategory.translate(translator)
    abv = abv.translate(translator)
    volume = volume.translate(translator)
    product_id = product_id.translate(translator).strip()

    #TODO: look into returning a json string

    product = {
        "name": name,
        "price": price,
        "category": category,
        "subcategory": subcategory,
        "abv": abv,
        "volume": volume,
        "product_id": product_id
    }

    return product

product = product_scrape("http://www.vinbudin.is/Heim/v%C3%B6rur/stoek-vara.aspx/?productid=12104/")
product_beer = product_scrape("http://www.vinbudin.is/Heim/v%C3%B6rur/stoek-vara.aspx/?productid=01215/")
print(product)
print(product_beer)
