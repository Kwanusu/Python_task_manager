# #requests - sends HTTPS requests
# #beautifulsoup - Parsing HTML & XML data

import requests

from bs4 import BeautifulSoup

# url = "https://zinduaschool.com/blog"

# response = requests.get(url)

# # print(response.content) 

# soup = BeautifulSoup(response.content, "html.parser")

# headings = soup.findall("h2")
# for heading in headings:
#    print(headings.text)


# url = "https://www.jumia.co.ke/recommended/"

# response = requests.get(url)

# # print(response.content) 

# soup = BeautifulSoup(response.content, "html.parser")

# products = soup.findall("h3", class_="name")
# for product in products:
#    print(products)
   
# # api_key=""
# # url = f"https://openweathermap.org/data/2.5/weather?q={location}&appid={api_key}"

# # posts = response.json()

# # for post in posts:
# #     print(post[post])

# url=requests.get(f"https://www.jumia.co.ke/mlp-black-friday/phones-tablets/?page=1")

url = "https://www.jumia.co.ke/catalog/productratingsreviews/sku/NI534ST0DQQMYNAFAMZ/"

response = requests.get(url)
 

soup = BeautifulSoup(response.content, "html.parser")

def get_reviews():
    
    response = requests.get(url)
 
    soup = BeautifulSoup(response.content, "html.parser")
    
    reviews = soup.find_all("h3", class_="-pvs")
    for review in reviews:
        print(reviews.text)
        
get_reviews(url)        
  
