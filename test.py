import pandas

data = pandas.read_csv("weather_data.csv")

print(data["temp"])

temp = data["temp"]

#avg = sum(temp) / len(temp)

#print(round(data["temp"].max(),2))

#print(data[data.temp == data.temp.max()])

monday = data[data.day == 'Monday']
monday_temp = monday.temp[0]
monday_temp_2 = monday.temp

print(monday_temp)
print(monday_temp_2)