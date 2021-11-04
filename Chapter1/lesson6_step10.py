from selenium import webdriver
import time

browser = webdriver.Chrome()
try:
    link = "http://suninjuly.github.io/registration1.html"
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    # elements = browser.find_elements_by_css_selector('input:required')
    # for element in elements:
    #     element.send_keys("Some text")

    first_name = browser.find_element_by_css_selector('input.first:required')
    first_name.send_keys("Oleg")
    last_name = browser.find_element_by_css_selector('input.second:required')
    last_name.send_keys("Kek")
    email = browser.find_element_by_css_selector('input.third:required')
    email.send_keys("oleg.kek@lolmail.com")

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(3)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(3)
    # закрываем браузер после всех манипуляций
    browser.quit()
