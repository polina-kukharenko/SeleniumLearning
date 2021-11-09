import time
import math
import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.parametrize('link', ['https://stepik.org/lesson/236895/step/1',
                                  'https://stepik.org/lesson/236896/step/1',
                                  'https://stepik.org/lesson/236897/step/1',
                                  'https://stepik.org/lesson/236898/step/1',
                                  'https://stepik.org/lesson/236899/step/1',
                                  'https://stepik.org/lesson/236903/step/1',
                                  'https://stepik.org/lesson/236904/step/1',
                                  'https://stepik.org/lesson/236905/step/1'])
def test_get_secret(link, browser):
    browser.get(link)

    WebDriverWait(browser, 3).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '.textarea'))
    ).send_keys(str(math.log(int(time.time()))))

    WebDriverWait(browser, 3).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.submit-submission'))
    ).click()

    pre = WebDriverWait(browser, 3).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, 'pre.smart-hints__hint'))
    )

    assert pre.text == 'Correct!', "Not 'Correct!'"
