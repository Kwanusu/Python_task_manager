
# Neccessary Imports
import requests
import csv
import pandas as pd
from bs4 import BeautifulSoup

url = "https://www.jumia.co.ke/mlp-black-friday/phones-tablets/?page=1"

# Product page Scrapper
def get_pagecontent(url):
    '''
    This helper function helps get the content from the site 
    and then gets to the required division so as to get the 
    required jumia products.
    parameter:
      url (str): a string of the cite you want to scrape
    returns:
      soup content(bs4 object):  from the required page
    '''
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        return soup
    else:
        print("Failed to retrieve the webpage.")
        return None

soup = get_pagecontent(url)

# Retrieve product name
def getproductname(soup):
    '''
    Helper function uses the soup object obtained from the product page
    and then extract product name
    parameter:
      soup (bs4Object) : a beautiful soup object containing parsed html
    returns:
      product_name (list) : list of product names
    '''
    product_name = [item.get_text() for item in soup.find_all("h3", class_="name")]
    return product_name

# Retrieve Brand Name
def getproductbrand(soup):
    '''
    Helper function uses the soup object obtained from the product page
    and then extracts product brand
    parameter:
      soup (bs4.BeautifulSoup) : a beautiful soup object containing parsed html
    returns:
      product_brand (list) : list of product brands
    '''
    product_brand = [item.get_text() for item in soup.find_all("div", class_="brand")]
    return product_brand

# Retrieve Price
def getproductprice(soup):
    '''
    Helper function uses the soup object obtained from the product page
    and then extract product price
    parameter:
      soup (bs4Object) : a beautiful soup object containing parsed html
    returns:
      product_price (list) : list of product prices
    '''
    product_price = [item.get_text() for item in soup.find_all("div", class_="prc")]
    return product_price

# Retrieve the Discount
def getproductdiscount(soup):
    '''
    Helper function uses the soup object obtained from the product page
    and then extract product discount
    parameter:
      soup (bs4Object) : a beautiful soup object containing parsed html
    returns:
      product_discount (list) : list of product discounts
    '''
    product_discount = [item.get_text() for item in soup.find_all("div", class_="tag _dsct _sm")]
    return product_discount

# Retrieve the Number of reviews.
def getproductreviewcnt(soup):
    '''
    Helper function uses the soup object obtained from the product page
    and then extract product review count
    parameter:
      soup (bs4Object) : a beautiful soup object containing parsed html
    returns:
      product_reviews (list) : list of product reviews
    '''
    product_reviewcnt = [item.get_text() for item in soup.find_all("div", class_="rev")]
    return product_reviewcnt

# Retrieve the ratings.
def getproductrating(soup):
    '''
    Helper function uses the soup object obtained from the product page
    and then extract product rating
    parameter:
      soup (bs4Object) : a beautiful soup object containing parsed html
    returns:
      product_rating (list) : list of product ratings
    '''
    product_rating = [item.get_text() for item in soup.find_all("div", class_="stars _s")]
    return product_rating

# Retrieve the remaining stock.
def getproductcount(soup):
    '''
    Helper function uses the soup object obtained from the product page
    and then extract remaining product stock
    parameter:
      soup (bs4Object) : a beautiful soup object containing parsed html
    returns:
      product_count (list) : list of product items remaining in stock
    '''
    product_count = [item.get_text() for item in soup.find_all("div", class_="stk _r")]
    return product_count

# Bonus Knowledge.
# Determine the actual customer satisfaction rating.
# this function will be computed using pandas
def getactualrating(reviews, rating):
    '''
    Helper function uses the review and rating columns obtained from the created dataframe
    and then calculate the final actual rating.
    parameter:
      reviews (list) : list of product reviews
      rating (list) : list of product ratings
    returns:
      actual_rating (list) : list of actual ratings
    '''
    df = pd.DataFrame({'reviews': reviews, 'rating': rating})
    df['actual_rating'] = df['rating'].astype(float) / df['reviews'].astype(int)
    actual_rating = df['actual_rating'].tolist()
    return actual_rating

# calling out the functions and creating a list of list containing the data
name = getproductname(soup)
brand = getproductbrand(soup)
price = getproductprice(soup)
discount = getproductdiscount(soup)
review = getproductreviewcnt(soup)
rating = getproductrating(soup)
count = getproductcount(soup)

list_of_lists = [name, brand, price, discount, review, rating, count]

# Save and review the product data
with open('jumia_products.csv', 'w', newline='') as jumia_file:
    fieldnames = ["name", "brand", "price", "discount", "reviews", "rating", "stock"]
    csvwriter = csv.writer(jumia_file)
    csvwriter.writerow(fieldnames)
    
    for product in zip(*list_of_lists):
        csvwriter.writerow(product)
        
    print("Done! All products have been added to CSV file")

# Using pandas to do data manipulation
jumia = pd.read_csv('jumia_products.csv')
jumia.head(10)
