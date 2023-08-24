import requests as rq
from datetime import datetime

# https://pixe.la/v1/user api

USERNAME = 'vedooo'
TOKEN = 'asgkğpwgpqmwpkgmpoqwe12312'
GRAPH_ID = 'graph1'

today = datetime(year=2023, month=7, day=23)

pixela_user_configs = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

headers = {
    "X-USER-TOKEN": TOKEN.encode('utf-8').decode('latin-1')   
}
pixela_graph_configs = {
    "id": "graph1",
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "kuro",
}

pixela_post_pixel_configs = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "12",
}

pixela_put_pixel_configs = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "15",
}

pixela_delete_pixel_configs = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "12",
}

pixela_url = 'https://pixe.la/v1/users'
pixela_url_graph = f'{pixela_url}/{USERNAME}/graphs'
pixela_url_post_pixel = f'{pixela_url_graph}/{GRAPH_ID}'
pixela_url_put_pixel = f'{pixela_url_graph}/{GRAPH_ID}/{today.strftime("%Y%m%d")}'
pixela_url_delete_pixel = f'{pixela_url_graph}/{GRAPH_ID}/{today.strftime("%Y%m%d")}'


response = rq.post(url=pixela_url, json=pixela_user_configs)
create_graph = rq.post(url=pixela_url_graph, json=pixela_graph_configs, headers=headers)
post_pixel = rq.post(url=pixela_url_post_pixel, json=pixela_post_pixel_configs, headers=headers)
put_pixel = rq.put(url=pixela_url_put_pixel, json=pixela_put_pixel_configs, headers=headers)
delete_pixel = rq.delete(url=pixela_url_delete_pixel, headers=headers)
