from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pandas as pd
from datetime import datetime # For manupilating dates
import os # Use terminal commands
import sys

app_path = os.path.dirname(sys.executable)
time = datetime.now()
day_mount_year = time.strftime("%a%d%m%Y")


url = 'https://www.thesun.co.uk/sport/football/'
chrome_options = webdriver.ChromeOptions()
chrome_options.headless = True
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(url=url)

containers = driver.find_elements(by='xpath', value='//div[@class="teaser__copy-container"]')

titles = []
subtitles = []
links = []

for container in containers:
    title = container.find_element(by='xpath', value='./a/span').text
    subtitle = container.find_element(by='xpath', value='./a/h3').text
    link = container.find_element(by='xpath', value='./a').get_attribute("href")
    titles.append(title)
    subtitles.append(subtitle)
    links.append(link)

thesun_dict = {
            'titles':titles,
            'subtitles': subtitles,
            'links': links
               }

df = pd.DataFrame(thesun_dict)
file_name = f'thesun_headline-{day_mount_year}.csv'
main_path = os.path.join(app_path, file_name)
df.to_csv(main_path)

driver.quit()

# using pyinstaller on windows = python -m PyInstaller 'filename'
# after that crontab script file