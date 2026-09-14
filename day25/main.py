
# with open('weather_data.csv') as file:
#     data = file.readlines()
#     data = data[1:]
#     print(data)

# import csv
# with open('weather_data.csv') as file:
#     data = csv.reader(file)
#     temperatures = []
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas
data = pandas.read_csv('weather_data.csv')
# temp_list = data['temp'].tolist()
# average = sum(temp_list) / len(temp_list)
# average_2 = data['temp'].mean()
# print(round(average, 2))
# print(round(average_2, 2))
max_temp = data.temp.max()
print(data[data.temp == max_temp])