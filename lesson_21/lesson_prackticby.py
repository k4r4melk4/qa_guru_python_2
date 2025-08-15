from pprint import pprint
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By # Инструмент By
from selenium.common.exceptions import NoSuchElementException # Исключение NoSuchElementException
from selenium.webdriver.remote.webelement import WebElement


# URL: str = 'https://books.toscrape.com/'
#
# option = webdriver.ChromeOptions() # создание объекта для настроек
# option.add_argument("--start-maximized") # указание полноэкранного отображения
#
# driver: webdriver.Chrome = webdriver.Chrome(options=option)
#
# driver.get(URL)


def get_driver() -> webdriver.Chrome:
    option: webdriver.ChromeOptions = webdriver.ChromeOptions()  # создание объекта для настроек
    option.add_argument("--start-maximized")
    return webdriver.Chrome(options=option)

def get_page(url: str, driver: webdriver.Chrome) -> None:
    driver.get(url)

def get_all_product_pods_on_page(driver: webdriver.Chrome) -> list[WebElement]:
    return driver.find_elements(By.CSS_SELECTOR, 'article.product_pod')

def get_all_data_from_product_page(product_pod: WebElement) -> dict[str, str]:
    h3_a_element: WebElement = product_pod.find_element(By.CSS_SELECTOR, 'h3 a')
    title: str = h3_a_element.get_attribute('title')
    href: str = h3_a_element.get_attribute('href')
    p_price_color_element: WebElement = product_pod.find_element(By.CSS_SELECTOR, 'p.price_color')
    price: str = p_price_color_element.text
    p_star_rating_element: WebElement = product_pod.find_element(By.CSS_SELECTOR, 'p.star_rating')
    rating: str = p_star_rating_element.get_attribute('class').split()[-1]
    return {
        'title': title,
        'href': href,
        'price': price,
        'rating': rating,
    }

def get_page_count(driver: webdriver.Chrome) -> int:
    current_element: WebElement = driver.find_element(By.CSS_SELECTOR, 'li.current')
    count_page: int = int(current_element.text.split()[-1])
    return count_page


def write_to_json(data: list(dict[str,str])) -> None:
    import json
    with open(data, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

def get_tabulete_table_from_list_dict(data: list[dict[str,str]]) -> str:
    # keys: list[str] = list(data[0].keys())
    # table: str = "<table_border = '1'>\n\t<tr>\n\t\t<th>" + "</th>\n\t\t<th>".join(keys) + "</th>\n\t</tr>"
    # # Добавляем строки
    #
    # for row in data:
    #     table += '\t<tr>\n\t\t<td>' + '</td>\n\\t\t<td>'.join(row.values()) + '</td>\n\t</tr>\n'
    #     table += "</table>"
    # return table
    from tabulate import tabulate
    return tabulate(data, headers='keys', tablefmt='github')

def main()
    driver: webdriver.Chrome = get_driver()

    get_pa