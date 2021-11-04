import time
import math

from selenium import webdriver


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = 'http://SunInJuly.github.io/execute_script.html'
with webdriver.Chrome() as browser:
    browser.get(link)
    x = browser.find_element_by_id('input_value').text
    browser.find_element_by_id('answer').send_keys(calc(int(x)))

    button = browser.find_element_by_css_selector('[type="submit"]')
    checkbox = browser.find_element_by_id('robotCheckbox')
    radio = browser.find_element_by_css_selector('[value="robots"]')

    browser.execute_script("return arguments[0].scrollIntoView(true);", radio)

    radio.click()
    checkbox.click()
    button.click()
    time.sleep(20)
