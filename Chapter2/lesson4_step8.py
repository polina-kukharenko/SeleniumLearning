import time
import math

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = 'http://suninjuly.github.io/explicit_wait2.html'
with webdriver.Chrome() as browser:
    browser.get(link)

    button = browser.find_element_by_id('book')
    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '$100')
    )
    button.click()

    x = browser.find_element_by_id('input_value').text
    browser.find_element_by_id('answer').send_keys(calc(int(x)))

    browser.find_element_by_css_selector('[type="submit"]').click()
    time.sleep(10)
