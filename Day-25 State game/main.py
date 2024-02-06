
# with open("weather_data.csv") as data_file:
#         data = data_file.readlines()
# #         gets saved into a list auto no need for appending into a list
#
# print(data)


import csv

with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
#     this creates a csv object
    temperatures = []
    for row in data:
        temperatures.append(int(row[1]))
        # prints all the data from row one which is temps into a array
    print(temperatures)


