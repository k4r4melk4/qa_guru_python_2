from time import sleep
from selenium import webdriver

URL = 'https://www.google.com'
option = webdriver.ChromeOptions()# создание объекта для настроек
# option.add_argument('') добавление настроек

option.add_argument("--window-size=1920,1080")#указание размера окна
option.add_argument("--start-maximized")#максимальное разрешение
option.add_argument("--disable-gpu")#отключение GPU
option.add_argument("--headless=new")#отключение отображения браузера

driver = webdriver.Chrome(options=option)
driver.get(URL)
sleep(2)
