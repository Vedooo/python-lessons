from bs4 import BeautifulSoup
import requests
import pandas as pd



def get_country_info():
    html_page = requests.get('https://www.scrapethissite.com/pages/simple/').text
    soup = BeautifulSoup(html_page, 'html.parser')
    rows = soup.find_all('div', class_='col-md-4 country')
    country_data = []
    
    for row in rows:
        country_name = row.find('h3').text.replace(' ','').strip()
        country_capital = row.find('span', class_='country-capital').text
        country_population = row.find('span', class_='country-population').text
        country_area = row.find('span', class_='country-area').text
        country_data.append({
            'Country Name': country_name,
            'Capital': country_capital,
            'Population': country_population,
            'Area': country_area
        })
    return country_data

data = get_country_info()
df = pd.DataFrame(data)

df.to_csv("countries.csv", index=False)