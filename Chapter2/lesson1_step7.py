import time
import math

from selenium import webdriver


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = 'http://suninjuly.github.io/get_attribute.html'
with webdriver.Chrome() as browser:
    browser.get(link)
    x = browser.find_element_by_id('treasure').get_attribute('valuex')
    browser.find_element_by_id('answer').send_keys(calc(int(x)))
    browser.find_element_by_id('robotCheckbox').click()
    browser.find_element_by_css_selector('[value="robots"]').click()
    browser.find_element_by_css_selector('[type="submit"]').click()
    time.sleep(10)
