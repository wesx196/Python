import pandas

data = pandas.read_csv("weather_data.csv")

#print(data["temp"])

temp = data["temp"]

#avg = sum(temp) / len(temp)

#print(round(data["temp"].max(),2))

#print(data[data.temp == data.temp.max()])

monday = data[data.day == 'Monday']
monday_temp = monday.temp[0]
monday_temp_2 = monday.temp

#print(monday_temp)
#print(monday_temp_2)

# numbers = [1,2,3]
# new_numbers = [n + 1 for n in numbers]
# print(new_numbers)

number_list = range(1,5)
double_list = [n * 2 for n in number_list]
print(double_list)