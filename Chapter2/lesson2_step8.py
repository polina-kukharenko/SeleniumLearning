import time
import os

from selenium import webdriver


link = 'http://suninjuly.github.io/file_input.html'
filepath = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'file.txt')

with webdriver.Chrome() as browser:
    browser.get(link)

    browser.find_element_by_css_selector('[name="firstname"]:required').send_keys('Oleg')
    browser.find_element_by_css_selector('[name="lastname"]:required').send_keys('Kek')
    browser.find_element_by_css_selector('[name="email"]:required').send_keys('test@lol.com')
    browser.find_element_by_id('file').send_keys(filepath)

    browser.find_element_by_css_selector('[type="submit"]').click()
    time.sleep(10)
