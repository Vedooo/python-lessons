import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


chrome_options = Options()
chrome_options.add_argument('--no-sandbox') # it'd not create any sandbox
chrome_options.add_argument('--headless') # It's going to run headles
chrome_options.add_argument('--disable-dev-shm-usage') # /dev/shm selenium's default memory usage path, disabling here and use /tmp from container



driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

url = 'https://www.neuralnine.com/books'

driver.get(url=url)

soup = BeautifulSoup(driver.page_source, features='lxml')

headings = soup.find_all(name='h2', attrs={'class': 'elementor-heading-title'})
for heading in headings:
    print(heading.getText())
    
    
time.sleep(10)

driver.quit()