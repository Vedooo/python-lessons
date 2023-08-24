from selenium import webdriver
from selenium.webdriver.common.by import By

# Keep browser open after program finished
chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_option)
# Amazon
# amazon_url = 'https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1'
# driver.get(url=amazon_url)

# price_dollar = driver.find_element(By.CLASS_NAME, value='a-price-whole')
# price_cents = driver.find_element(By.CLASS_NAME, value='a-price-fraction')
# print(f'The price is {price_dollar.text}.{price_cents.text}')

# Python
# python_url = 'https://www.python.org'
# driver.get(url=python_url)
# search_bar = driver.find_element(By.NAME, value='q')
# print(search_bar.tag_name)
# print(search_bar.get_attribute("placeholder"))

# button = driver.find_element(By.ID, value='submit')
# print(button.size)

# documentation_link = driver.find_element(By.CSS_SELECTOR, value='.documentation-widget a')
# print(documentation_link.text)

# find_by_xpath = driver.find_element(By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(find_by_xpath.text)

# python_url = 'https://www.python.org'
# driver.get(url=python_url)

# event_times = driver.find_elements(By.CSS_SELECTOR, value='.event-widget time')
# event_names = driver.find_elements(By.CSS_SELECTOR, value='.event-widget li a')
# events = {}

# for n in range(len(event_times)):
#     events[n] = {
#         "time": event_times[n].text,
#         "name": event_names[n].text,
#     }

# print(events)

# driver.close() # Close the current tab on browser
driver.quit() # Close the all browser and tabs

