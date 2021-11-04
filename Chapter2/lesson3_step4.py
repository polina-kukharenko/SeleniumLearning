import time
import math

from selenium import webdriver


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = 'http://suninjuly.github.io/alert_accept.html'
with webdriver.Chrome() as browser:
    browser.get(link)

    browser.find_element_by_css_selector('[type="submit"]').click()
    confirm = browser.switch_to.alert
    confirm.accept()

    x = browser.find_element_by_id('input_value').text
    browser.find_element_by_id('answer').send_keys(calc(int(x)))

    browser.find_element_by_css_selector('[type="submit"]').click()
    time.sleep(10)
