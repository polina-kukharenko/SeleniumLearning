import time

from selenium import webdriver
from selenium.webdriver.support.ui import Select


# link = 'http://suninjuly.github.io/selects1.html'
link = 'http://suninjuly.github.io/selects2.html'
with webdriver.Chrome() as browser:
    browser.get(link)

    num1 = browser.find_element_by_id('num1').text
    num2 = browser.find_element_by_id('num2').text
    sum = int(num1) + int(num2)

    select = Select(browser.find_element_by_id("dropdown"))
    select.select_by_value(str(sum))
    browser.find_element_by_css_selector('[type="submit"]').click()

    time.sleep(10)
