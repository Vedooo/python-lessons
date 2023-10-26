import mysql.connector
from selenium import webdriver
import random as rd
import json

db_connection = mysql.connector.connect(
    host = "127.0.0.1",
    user = "root",
    password = "159357",
    database = "testdb"
)

cursor = db_connection.cursor()
cursor.execute("CREATE TABLE recipies ( \
                food_name VARCHAR(255), \
                category VARCHAR(255), \
                rating VARCHAR(255), \
                link VARCHAR(255) \
                )"
            )


url = 'https://www.allrecipes.com/recipes/17057/everyday-cooking/more-meal-ideas/5-ingredients/main-dishes/'
chrome_options = webdriver.ChromeOptions()
chrome_options.headless = True
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(url=url)
recipies = []

for i in range(4):
    if i == 0:
        containers = driver.find_elements(by='xpath', value=f'//div[@id="tax-sc__recirc-list_1-0"]/a')
    else:
        containers = driver.find_elements(by='xpath', value=f'//div[@id="tax-sc__recirc-list_1-0-{i}"]/a')
    
    for container in containers:
        link = container.get_attribute("href")
        category = container.find_element(by='xpath', value='./div[2]').get_attribute("data-tag")
        food_name = container.find_element(by='xpath', value='./div[2]/span/span').text
        rating = container.find_element(by='xpath', value='./div[2]/div[@class="comp recipe-card-meta"]/div/div[2]').text
        recipies.append({
                "food_name": food_name,
                "category": category, 
                "rating": rating, 
                "link": link,
            })

with open("recipies.json", "w") as file:
    json.dump(recipies, file, indent=4)

driver.quit()

recipies_as_tuples = [(item['food_name'], item['category'], item['rating'], item['link']) for item in recipies]

formula = "INSERT INTO recipies (food_name, category, rating, link) VALUES (%s, %s, %s, %s)"
cursor.executemany(formula, recipies_as_tuples)
db_connection.commit()
