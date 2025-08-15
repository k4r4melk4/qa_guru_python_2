from pprint import pprint
from time import sleep
from traceback import print_tb

from pyexpat.errors import messages
from selenium import webdriver
from selenium.webdriver.common.by import By # Инструмент By
from selenium.common.exceptions import NoSuchElementException # Исключение NoSuchElementException
from selenium.webdriver.remote.webelement import WebElement

LOCAL_FILE = r'/cities/index.html'  # r строка
URL = 'https://books.toscrape.com/'

option = webdriver.ChromeOptions() # создание объекта для настроек
option.add_argument("--start-maximized") # указание полноэкранного отображения

# создание драйвера с настройками
driver: webdriver.Chrome = webdriver.Chrome(options=option)

# Переходим на страницу

# поиск элемента по имени тега body - возвращает один элемент
# (одно и тоже, просто разные тайп хинты )
# body_element: webdriver.remote.webelement.WebElement = driver.find_element(By.TAG_NAME, "body")
# body_element: WebElement = driver.find_element(By.TAG_NAME, "body")


# Пример работы с инструментом By.ID messages
# messages_element - переменная
# : WebElement - аннотация типов
# divs_blocks: WebElement = driver.find_element(By.ID, '1')
# text_element: str = divs_blocks.text
#
# print(type(divs_blocks))
# print(text_element.split('\n'))
#
# # погружаемся глубже и ищем элемент с id = div3
# div3_block: WebElement = divs_blocks.find_element(By.ID, 'div-1')
#
# text_div3_element: str = div3_block.text
#
# print(text_div3_element)

# driver.get(LOCAL_FILE)


# Пример работы с инструментом By.CLASS_NAME
# find_element - возвращает первый попавшийся
# find_elements - возвращает все
# divs_block: WebElement = driver.find_element(By. CLASS_NAME, 'flex-container')
# print(divs_block.text.split())
# inner_div: list[WebElement] = divs_block.find_elements(By.CLASS_NAME, 'flex-item')
# print(type(inner_div))
# print(len(inner_div))
# print(inner_div[0].text)

# #открываем сайт
# #выбтираем все элементы с class_name = product_pod
# product_cards: list[WebElement] = driver.find_elements(By.CLASS_NAME, "product_pod")
#
# for product_card in product_cards:
#     print('-' * 10)
#     print(product_card.text)

# Пример работы с инструментом By.TAG_NAME

# h2_elements: list[WebElement] = driver.find_elements(By.TAG_NAME, "h2")
# [print(h2_element.text) for h2_element in h2_elements]

#
# driver.get(URL)
# #ищем все карточки товара по CLASS_NAME = product_pod
# product_cards: list[WebElement] = driver.find_elements(By.CLASS_NAME, "product_pod")
# # создаем пустой список product_title для хранения заголовков
# product_title: list[str] = []
# #инициализируем перебор списка product_card
# for product_card in product_cards:
#     #находим заголовок product_card
#     card_h3: WebElement = product_card.find_element(By.TAG_NAME, "h3")
#     #добавляем текст из заголовка h3 в список product_title
#     product_title.append(card_h3.text)
#
# print(product_title)


# Пример работы с инструментом By.NAME
# driver.get(LOCAL_FILE)
# first_name_element: WebElement = driver.find_element(By.NAME, "firstname")
# first_name_element.send_keys('Иван')
#
# sleep(2)


# Пример работы с инструментом By.LINK_TEXT и By.PARTIAL_LINK_TEXT

# TEXT_LINK: str = 'A Light in the ...'
# driver.get(URL)
#
# # ищем элемент с текстом A light in the ... - полное вхождение
# link_element: WebElement = driver.find_element(By.LINK_TEXT, TEXT_LINK)
# link_element.click()
# sleep(5)
#
# # возвращаемся назад
# driver.back()
#
# # ищем элемент с текстом Light in the - частичное вхождение
# link_element: WebElement = driver.find_element(By.PARTIAL_LINK_TEXT, 'Light in the')
# link_element.click()
# sleep(5)


# Пример работы с инструментом By.CSS_SELECTOR

driver.get(URL)

#ищем все элементы article.product_pod
product_cards: list[WebElement] = driver.find_elements(By.CSS_SELECTOR, 'article.product_pod')

#создаем пустой список для заголовков
product_titles: list[str] = []
product_href: dict[str, str] = {}

#перебираем все карточки
for product_card in product_cards:
    # ищем все элементы h3 a
    title_card: WebElement = product_card.find_element(By.CSS_SELECTOR, 'h3 a')
    # добываем заголовок
    title: str = title_card.get_attribute("title")
    # добываем заголовок
    href: str = title_card.get_attribute("href")

    product_titles.append(title)
    product_href.update(
        {
            title:href
        }
    )
pprint(product_titles)
pprint(product_href)


