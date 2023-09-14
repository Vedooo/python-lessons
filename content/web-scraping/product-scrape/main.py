import json
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

URL = f'https://www.alibaba.com/trade/search?spm=a2700.galleryofferlist.0.0.76f76e0cTCMUlZ&fsb=y&IndexArea=product_en&keywords=paracord&&page=1'

driver = webdriver.Chrome()
driver.get(URL)


def filter_checks():
    verified_supplier = driver.find_element(By.XPATH, value='//*[@id="root"]/div/div[4]/div/div[5]/div[2]/a[1]/label/span[1]')
    verified_supplier.click()
    time.sleep(5)
    ready_to_ship = driver.find_element(By.XPATH, value='//*[@id="root"]/div/div[4]/div/div[6]/div[2]/a[1]/label/span[1]')
    ready_to_ship.click()
    time.sleep(5)


filter_checks()

scroll_pause_time = 3
screen_height = driver.execute_script("return window.screen.height;")
i = 1
while True:
    driver.execute_script("window.scrollTo(0, {0}*{1});".format(i, screen_height))
    time.sleep(scroll_pause_time)
    i += 1
    if i > 10:
        break

url_text = driver.page_source
soup = BeautifulSoup(url_text, 'html.parser')

items = soup.find_all('div', class_="card-info list-card-layout__info")
item_list = []
product_id = 0

for item in items:
    product_id += 1
    title = item.find('h2', class_="search-card-e-title").text
    price = item.find('div', class_="search-card-e-price-main").text
    order_info = item.find_all('div', class_="search-card-m-sale-features margin-bottom-12")
    for info_container in order_info:
        info_items = info_container.find_all('div', class_="search-card-m-sale-features__item")
    experience = driver.find_element(By.XPATH, value='//*[@id="root"]/div/div[5]/div[3]/div/div/div/div[1]/div[2]/div[1]/div[1]/div/a[3]/span').text
    item_list.append({
        f"{int(product_id)}": {
            "title": title,
            "price": price,
            "info": {info.text for info in info_items},
            "experience": experience.replace('\n', ' '),
            }
        })

print(item_list)

driver.quit()
