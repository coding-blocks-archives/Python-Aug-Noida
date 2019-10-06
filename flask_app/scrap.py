import requests
from bs4 import BeautifulSoup

def scrap_snapdeal(query):
  url = "https://www.snapdeal.com/search"
  params = {
      "keyword": query
  }
  r = requests.get(url, params=params)
  soup = BeautifulSoup(r.content)
  products = soup.findAll('div', attrs = {"class": "product-tuple-listing"})

  result = []

  for product in products:
    name = product.find('p', attrs={"class": "product-title"}).text
    img = product.find('img')
    if 'src' in img.attrs:
        image = img.attrs['src']
    else:
        image = img.attrs['data-src']
    
    result.append((name, image))

  return result