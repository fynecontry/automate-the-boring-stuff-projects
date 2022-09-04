#!/usr/bin/env python3
# img_downloader.py     - searches flickr for CLI provided word and 
#                       downloads 10 images into a folder

import sys, os, logging, requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# keyword obtained from CLI
if len(sys.argv) < 2:
    print('usage: img_downloader.py [search_keyword]')
    sys.exit(1)

else:
    search_keyword = ' '.join(sys.argv[1:])

# Open browser and redirect to flickr
browser = webdriver.Chrome()
browser.get('https://www.flickr.com/')


# TODO: Search site using search_keyword


# TODO: Download # of images


# TODO: Write images to folder 
