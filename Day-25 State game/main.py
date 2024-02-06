
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

import pandas

data = pandas.read_csv("weather_data.csv")
# print(data["temp"])


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


#Create a dataframe from scratch
data_dict = {
    "students": ["Amy","Ryan"],
    "scores" : [65,23]
}

# used to create a csv from panda library
data = pandas.DataFrame(data_dict)
print(data)
data.to_csv("new_data.csv")