from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import json
import os


class ImageCrawler(object):
    def __init__(self, search_term, num_to_search, out_dir):
        url = "https://www.google.co.in/search?q=" + search_term + "&tbm=isch"
        browser = webdriver.Chrome("chromedriver.exe")
        browser.get(url)
