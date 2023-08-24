from bs4 import BeautifulSoup
from sqlalchemy import create_engine
import requests
import pandas as pd


USERNAME = 'root'
PASSWORD = ''
DATABASE = 'teams'
HOST     = 'localhost'


def get_team_data():
    url = requests.get('https://www.scrapethissite.com/pages/forms/').text
    soup = BeautifulSoup(url, 'html.parser')

    teams = soup.find_all('tr', class_='team')
    team_data = []

    for team in teams:
        name   = team.find('td', class_='name').text.strip()
        year   = team.find('td', class_='year').text.strip()
        wins   = team.find('td', class_='wins').text.strip()
        losses = team.find('td', class_='losses').text.strip()
        pct    = team.find('td', class_='pct').text.strip()
        gf     = team.find('td', class_='gf').text.strip()
        ga     = team.find('td', class_='ga').text.strip()
        diff   = team.find('td', class_='diff').text.strip()
        team_data.append({
            'name': name,
            'year': year,
            'wins': wins,
            'losses': losses,
            'pct': pct,
            'gf': gf,
            'ga': ga,
            'diff': diff
        })    
    return team_data

data = get_team_data()
df = pd.DataFrame(data)

df.to_csv('teams.csv', index=True)

engine = create_engine('mysql+pymysql://' + USERNAME + ':' + PASSWORD + '@' + HOST + '/' + DATABASE)
df.to_sql(con=engine, name='teams', if_exists='append', index=False)