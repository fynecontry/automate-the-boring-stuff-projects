#!/usr/bin/env python3
# cli_emailer.py    -   A CLI tool which takes email addresses
#                   and message as args and send email to dest.

import sys, logging
import time
import pyinputplus as pyip
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')

# Extract email addresses & message
if len(sys.argv) != 4:
    print('usage: cli_emailer.py [source] [destination] [message]')
    sys.exit(1)

else:
    source_email = sys.argv[1]
    destination_email = sys.argv[2]
    message = sys.argv[3]

# Prompt for users sign in password
user_password = pyip.inputPassword(f'{source_email} password: ')

# Intiate browser session & login to mail
browser = webdriver.Chrome()
browser.get('https://mail.google.com/')

username_elem = browser.find_element(By.ID, 'identifierId')
username_elem.clear()
username_elem.send_keys(source_email)
username_elem.send_keys(Keys.RETURN)
logging.info('user email accepted')
time.sleep(20)
password_elem = browser.find_element(By.XPATH,'//*[@id ="password"]/div[1]/div / div[1]/input')
password_elem.clear()
password_elem.send_keys(user_password)
password_elem.send_keys(Keys.RETURN)
logging.info('Sign in successful')


# draft email body
browser.get('https://mail.google.com/mail/u/0/#inbox?compose=new')
recipient_elem = browser.find_element(By.XPATH, '//textarea[@id=":95"]')
recipient_elem.clear()
recipient_elem.send_keys(destination_email)


# TODO: Send email
