
# with open("weather_data.csv") as data_file:
#         data = data_file.readlines()
# #         gets saved into a list auto no need for appending into a list
#
# print(data)

#
# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
# #     this creates a csv object
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#         # prints all the data from row one which is temps into a array
#     # print(temperatures)
#
# import pandas
#
# data = pandas.read_csv("weather_data.csv")
# # print(data["temp"])
#

# data_dict = data.to_dict()
# # print(data_dict)
#
# temp_list = data["temp"].tolist()
# # print(temp_list)
# total = 0

# print(data["temp"].max())

# print(data.condition)

# get data in row
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# print(monday.temp)
# print((monday.temp * 9/5) + 32)

#
# #Create a dataframe from scratch
# data_dict = {
#     "students": ["Amy","Ryan"],
#     "scores" : [65,23]
# }

# used to create a csv from panda library
# data = pandas.DataFrame(data_dict)
# print(data)
# data.to_csv("new_data.csv")

import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240207.csv")
red = 0
grey = 0
black = 0


# grey_squirrel_count = len(data[data["Primary Fur Color"] == "Gray"])
# red_squirrel_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
# black_squirrel_count = len(data[data["Primary Fur Color"] == "Black"])

# can use this loop or this code above to access all the data from the csv


for color in data["Primary Fur Color"]:
    if color == "Cinnamon":
        red +=1
    elif color == "Gray":
        grey +=1
    else:
        black +=1

print(data["Primary Fur Color"])
data_dict = {
    "Fur color": ["Grey","Cinnamon","Black"],
    "Count": [grey,red,black]
}
new_data = pandas.DataFrame(data_dict)
new_data.to_csv("Squirrel_Colors.csv")