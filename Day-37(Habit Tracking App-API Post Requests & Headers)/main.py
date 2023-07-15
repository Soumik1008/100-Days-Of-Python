import requests
from datetime import datetime

USERNAME = "bunty"
TOKEN = "div08yan10sh20iiqt00"
GRAPH_ID = "graph1"
pixela_endpoint = "https://pixe.la/v1/users"

user_params={
    "token":USERNAME,
    "username":TOKEN,
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}

# Creating a User
# response = requests.post(url=pixela_endpoint,json=user_params)
# print(response.text)

graph_config = {
    "id":"graph1",
    "name":"Cycling Graph",
    "unit":"Km",
    "type":"float",
    "color":"ajisai"
}

headers = {
    "X-USER-TOKEN":TOKEN
}

# graph_endpont = f"{pixela_endpoint}/{USERNAME}/graphs"
# response = requests.post(url = graph_endpont, json=graph_config, headers=headers)
# print(response.text)

pixel_creation_endpont = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime(year=2023,month=7,day=13)

pixel_data = {
    "date":today.strftime("%Y%m%d"),
    "quantity":input("How many kilometres did you cycle today?")
}

response = requests.post(url=pixel_creation_endpont, json=pixel_data, headers=headers)
print(response.text)

# updated_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

# new_pixel_data = {
#     "quantity":"6.86"
# }

# response = requests.put(url=updated_pixel_endpoint, json=new_pixel_data, headers=headers)
# print(response.text)

# delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)