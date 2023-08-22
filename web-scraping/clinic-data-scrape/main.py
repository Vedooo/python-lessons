import requests
import pandas as pd
from bs4 import BeautifulSoup

start = 12000
end = 12010

br_sorry   = "Sorry, we can't find that practice. Make sure you typed the right address."
br_payment = "Payment Confirmation"

def get_clinic_name(clinic_id):
    url         = f'https://{clinic_id}.portal.athenahealth.com/'
    response    = requests.get(url)
    html        = response.text
    soup        = BeautifulSoup(html, 'html.parser')
    clinic_name = soup.find_all('h1')[-1].text.strip()
    return clinic_name

master_list = []

for clinic_id in range(start,end):
    data_dict = {}
    data_dict['clinic_id'] = clinic_id
    data_dict['clinic_name'] = get_clinic_name(clinic_id)
    if data_dict["clinic_name"] != br_sorry and data_dict["clinic_name"] != br_payment:
        master_list.append(data_dict)
    
df = pd.DataFrame(master_list)
df.to_csv("clinic_names.csv")
print("Done..")