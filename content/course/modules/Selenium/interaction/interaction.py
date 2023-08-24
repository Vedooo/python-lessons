from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_option)
driver.maximize_window()

# driver.get(url='https://en.wikipedia.org/wiki/Main_Page')
# article_count = driver.find_element(By.XPATH, value='//*[@id="articlecount"]/a[1]')
# article_count.click()

# search_bar = driver.find_element(By.NAME, value='search')
# search_bar.send_keys("Mustafa Kemal Ataturk")
# search_bar.send_keys(Keys.ENTER)

driver.get(url='http://secure-retreat-92358.herokuapp.com')

name_input = driver.find_element(By.NAME, value='fName')
name_input.send_keys("Vedooo")
lname_input = driver.find_element(By.NAME, value='lName')
lname_input.send_keys("Toss")
email_input = driver.find_element(By.NAME, value='email')
email_input.send_keys("toss@gmail.com")
sign_up = driver.find_element(By.CLASS_NAME, value='btn')
sign_up.click()
