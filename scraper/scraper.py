import requests
import json

from datetime import date
from bs4 import BeautifulSoup

def getAmazonPrice(url):
    webpage = requests.get(url)
    soup = BeautifulSoup(webpage.content, "html.parser")
    price = int(soup.find("span", class_ = "a-price-whole").getText().removesuffix(".")) + int(soup.find("span", class_ = "a-price-fraction").getText())/100 
    return price

def getAmazonItemName(url):
    webpage = requests.get(url)
    soup = BeautifulSoup(webpage.content, "html.parser")
    name = soup.find("span", id="productTitle").getText()
    return name

def makeItem(url):
    name = getAmazonItemName(url)
    price = getAmazonPrice(url)
    today = str(date.today())
    item = {"name": name, "last-checked": today, "current-price": price, "lowest-price": price, "url": url}
    return item

def updateItem(item):
    url = item["url"]
    name = getAmazonItemName(url)
    price = getAmazonPrice(url)
    lowest_price = item["lowest-price"]
    today = str(date.today())
    if price < lowest_price:
        lowest_price = price
    new_item =  {"name": name, "last-checked": today, "current-price": price, "lowest-price": lowest_price, "url": url}
    return new_item

def saveItems(items):
    itemsJson = json.dumps(items)
    with open("data.json", "w") as jsonFile:
        jsonFile.write(itemsJson)

def getSavedItems():
    try:
        with open("data.json", "r") as jsonFile:
            items = json.load(jsonFile)
    except:
        items = []
    return items

def addItem(item):
    items = getSavedItems()
    items.append(item)
    saveItems(items)

def removeItem(index):
    items = getSavedItems()
    items.pop(index)
    saveItems(items)