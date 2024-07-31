import requests
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users" 

TOKEN = "ilikewafflesalot"
USERNAME = "michal8"

user_params = {
    "token" : TOKEN,
    "username" : USERNAME,
    "agreeTermsOfService" : "yes",
    "notMinor" : "yes"

}

# response = requests.post(url=pixela_endpoint,json=user_params)

# graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
GRAPHID = "graph1"
# graph_params = {
#     "id" : GRAPHID,
#     "name" : "Piano Practice Tracker",
#     "unit": "min",
#     "type" : "int",
#     "color" : "ajisai"
# }

headers = {
    "X-USER-TOKEN" : TOKEN
}

# response = requests.post(url=graph_endpoint,json=graph_params, headers=headers)
# print(response.text)


today = datetime.now().strftime("%Y%m%d")

post_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}"

pixel_params = {
    "date" : today,
    "quantity" : input("How many minutes did you practice for today? "),
}

response = requests.post(url=post_pixel_endpoint,json=pixel_params,headers=headers)

print(response.text)