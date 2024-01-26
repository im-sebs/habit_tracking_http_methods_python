import requests
import datetime

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
USERNAME = "sebs"
TOKEN = "hola1234"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
#
# response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
# print(response.text)

graph_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
GRAPH_ID = "graph1"

graph_params = {
    "id": GRAPH_ID,
    "name": "Meditation",
    "unit": "Times",
    "type": "int",
    "color": "kuro"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)

value_graph_endopint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"


today = datetime.date.today()
#POST
# value_params = {
#     "date": today.strftime("%Y%m%d"),
#     "quantity": "25"
# }
#
# response = requests.post(url=value_graph_endopint, json=value_params, headers=headers)

#PUT
# value_params = {
#     "color": "ichou"
# }
#
# response = requests.put(url=value_graph_endopint, json=value_params, headers=headers)

#DELETE

response = requests.delete(url=value_graph_endopint, headers=headers)
print(response.text)
