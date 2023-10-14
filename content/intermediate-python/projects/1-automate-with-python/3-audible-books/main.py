from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import logging

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

scrape_page = True

while scrape_page:
    scroll_down(4)
    click_next_page()

# containers = driver.find_element()



driver.quit()

