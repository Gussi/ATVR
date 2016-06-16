def scrape_all():
    # Web 2.0 sucks

    import requests
    import json

    sesh = requests.Session()
    sesh.max_redirects = 5

    url = "http://www.vinbudin.is/addons/origo/module/ajaxwebservices/search.asmx/DoSearch"
    #Custom headers to get around the dreaded 500 response
    headers = {
        "Host": "www.vinbudin.is",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate",
        "Content-Type": "application/json; charset=utf-8",
        "X-Requested-With": "XMLHttpRequest",
        "Referer": "http://www.vinbudin.is/Heim/v%C3%B6rur/v%C3%B6rur.aspx?",
        "Connection": "keep-alive"
    }

    # The site is paginated, but I don't know how many products there are for sale, 
    # so I start with requesting 0 products, because it returns the total amount of products for sale
    payload = {"skip": 0, "count": 0, "orderBy": "random"}

    response = sesh.get(url, headers=headers, params=payload)
    if response.status_code == 500:
        print("Site returned 500! :(")
        quit()

    total = json.loads(response.json()["d"])["total"]

    # after I know the total, I can request all the rest of the items with a single GET :D
    payload["count"] = total

    response = sesh.get(url, headers=headers, params=payload)
    jsonresponse = response.json()
    products = json.loads(jsonresponse["d"])
    data = products["data"]

    allthestuff = []

    for d in data:
        product = {
            "name": d["ProductName"],
            "price": d["ProductPrice"],
            "abv": d["ProductAlchoholVolume"],
            "volume": d["ProductBottledVolume"],
            "product_id": d["ProductID"],
            "country": d["ProductCountryOfOrigin"],
            "category": d["ProductCategory"]["name"]
        }
        allthestuff.append(product)
    return allthestuff
