# csv files
import csv

with open ('weather_data.csv') as data_file:
    data = csv.reader(data_file)
    temperatures = []
    for row in data:
        if row[1] != 'temp':
            temperatures.append(int(row[1]))
print(temperatures)

# pandas
import pandas

data = pandas.read_csv('weather_data.csv')
print(data['temp'])

data_dict = data.to_dict()
print(data_dict)

temp_lst = data['temp'].to_list()
print(temp_lst)

avg_temp = sum(temp_lst) / len(temp_lst)
print(avg_temp)
print(data['temp'].mean())

print(data['temp'].max())

#get row of data

row = data[data.day == "Monday"]
print(row)

max_temp_row = data[data.temp == data.temp.max()]
print(max_temp_row)
print(max_temp_row.condition)

def convert_to_fahrenheit(celsius_temp):

    return (celsius_temp * 9/5) + 32

max_temp_fahrenheit = convert_to_fahrenheit(max_temp_row.temp)
print(f"{max_temp_fahrenheit}")

# create dataframe from scratch

data_dict = {
    "students": ['bob', 'vic'],
    "scores": [56, 67]
}
data = pandas.DataFrame(data_dict)
print(data)

data.to_csv('student-scores.csv')








