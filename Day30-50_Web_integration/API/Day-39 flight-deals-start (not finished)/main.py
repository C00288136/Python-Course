from data_manager import DataManager
from flight_search import FlightSearch
#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

Manager = DataManager()

sheet_data = Manager.get_destination_data()


# if sheet_data[0]["iataCode"] == "":
#     from flight_search import FlightSearch
#     flight_search = FlightSearch()  
#     for row in sheet_data:
#         row["iataCode"] = flight_search.get_destination_code(row["city"])
#     print(f"sheet_data:\n {sheet_data}")

#     Manager.destination_data = sheet_data
#     Manager.update_destination_codes()

token = FlightSearch()

        
        





