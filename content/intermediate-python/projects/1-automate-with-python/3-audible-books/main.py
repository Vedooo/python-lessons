from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import logging
import json

SCROLL_PAUSE_TIME = 1

def scroll_down(scroll_count: int):
    try:
        screen_height = driver.execute_script("return window.screen.height;")
        i = 1
        while True:
            driver.execute_script("window.scrollTo(0, {0}*{1});".format(i, screen_height))
            time.sleep(SCROLL_PAUSE_TIME)
            i += 1
            if i > scroll_count:
                break
            
    except Exception as e:
        logging.error(f'Error scroll page: str{e}')

def click_next_page():
    list = driver.find_element(by='xpath', value='//*[@id="pagination-a11y-skiplink-target"]/div/div[2]/div/span/ul')
    list_items = list.find_elements('xpath', value='./li')
    last_item = list_items[-1]
    last_item.click()
	
url = 'https://www.audible.com/search'
chrome_options = webdriver.ChromeOptions()
chrome_options.headless = False
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(url=url)

book_list = []
scrape_open = True
index = 1
while scrape_open:
    containers = driver.find_elements(by='xpath', value='//*[@id="center-3"]/div/div/div/span[2]/ul')
    for container in containers:
        books = container.find_elements(by='xpath', value=f'./li[{index}]/div/div[1]/div/div[2]/div/div/span/ul')
        for book in books:
            name = book.find_element(by='xpath', value='./li[1]/h3/a').text
            link = book.find_element(by='xpath', value='./li[1]/h3/a').get_attribute("href")
            sub_title = book.find_element(by='xpath', value='./li[2]/span').text
            author = book.find_element(by='xpath', value='./li[3]/span/a').text
            author_link = book.find_element(by='xpath', value='./li[3]/span/a').get_attribute("href")
            book_list.append({
                "name": name,
                "link": link,
                "sub_title": sub_title,
                "author": author,
                "author_links": author_link,
            })
        index += 1    
        if index > 20:
            click_next_page()
            index = 1 

        with open("book_list.json", "w") as file:
            json.dump(book_list, file, indent=4)

driver.quit()

