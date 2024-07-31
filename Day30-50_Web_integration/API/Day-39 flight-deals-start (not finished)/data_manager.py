import os
import requests
from requests.auth import HTTPBasicAuth
from pprint import pprint
from dotenv import load_dotenv

load_dotenv()

GET_ENDPOINT  = "https://api.sheety.co/cb8eb9e122d16917dde918fcd63ff04e/flightDeals/prices"


class DataManager:
    


    
    def __init__(self):
        self._user = os.environ["SHEETY_USRERNAME"]
        self._password = os.environ["SHEETY_PASSWORD"]
        # autherization used so the api can only be accessed if variables are true
        self._authorization = HTTPBasicAuth(self._user, self._password)
        self.destination_data = {}
        
        
        # function to retrieve the data from the sheet
    def get_destination_data(self):
        
        response = requests.get(url=GET_ENDPOINT, auth=self._authorization)
        data = response.json()
        self.destination_data = data["prices"]
        # pprint(data)

        return self.destination_data
    

# fucntion to update the iatacode for each flight
    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(url=f"{GET_ENDPOINT}/{city['id']}", json=new_data, auth=self._authorization)
            print(response.text)

        
        
        
