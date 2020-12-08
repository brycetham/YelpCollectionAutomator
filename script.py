from selenium import webdriver
import os
import re

import argparse
import json
import pprint
import requests
import sys
import urllib

from urllib2 import HTTPError
from urllib import quote
from urllib import urlencode

API_KEY = ""
API_HOST = 'https://api.yelp.com'
SEARCH_PATH = '/v3/businesses/search'

def startDriver():
    PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
    DRIVER_BIN = os.path.join(PROJECT_ROOT, "chromedriver")
    driver = webdriver.Chrome(executable_path = DRIVER_BIN)
    return driver

def getRestaurantsList():
    file = open("check_in.html", "r")
    table = file.read()
    regex = r"<tr>.+?<td>.+?<td>\s*(.+?)\s*<\/td>.+?<td>.+?<td>\s*(.+?)\s*<\/td>.+?<td>\s*(.+?)\s*<\/td>.+?<\/tr>"
    matches = re.findall(regex, table, re.MULTILINE | re.DOTALL)
    return matches

def getRestaurantURL(name, longitude, latitude):
    print(name, longitude, latitude)
    name = "Rita's Italian Ice"
    url_params = {
        'term': name.replace(' ', '+'),
        'longitude': float(longitude),
        'latitude': float(latitude),
        'limit': 1,
        'sort_by': 'distance'
    }
    print(url_params)
    url = '{0}{1}'.format(API_HOST, quote(SEARCH_PATH.encode('utf8')))
    headers = {
        'Authorization': 'Bearer %s' % API_KEY
    }
    response = requests.request('GET', url, headers=headers, params=url_params)
    business = response.json()["businesses"][0]
    print(business["name"], business["url"])
    return business["url"]

def quitDriver(driver):
    driver.quit()

if __name__ == '__main__':
    driver = startDriver()

    matches = getRestaurantsList()
    for name, longitude, latitude in reversed(matches):
        url = getRestaurantURL(name, longitude, latitude)
        driver.get(url)

    input('Collection complete. Press ENTER to close the automated browser.')
    driver.quit()
