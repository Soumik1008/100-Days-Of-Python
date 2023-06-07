# import csv
# with open('Day-25(Working with CSV and Pandas)\weather_data.csv') as data_file:
#     data = csv.reader(data_file)
#     temperature=[]    
#     for row in data:
#         if(row[1]!='temp'):
#             temperature.append(int(row[1]))
#     print(temperature)

import pandas
data = pandas.read_csv("Day-25(Working with CSV and Pandas)\squirrel.csv")

grey_squirrels_data_count = len(data[data['Primary Fur Color']=='Gray'])
red_squirrels_data_count = len(data[data['Primary Fur Color']=='Cinnamon'])
black_squirrels_data_count = len(data[data['Primary Fur Color']=='Black'])

print(grey_squirrels_data_count)
print(red_squirrels_data_count)
print(black_squirrels_data_count)

data_dict = {
    "Fur Color":["Gray","Cinnamon","Black"],
    "Count":[grey_squirrels_data_count,red_squirrels_data_count,black_squirrels_data_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv('Day-25(Working with CSV and Pandas)\Squirrel_count.csv')

# print(type(data))
# print(type(data['temp']))
# print(data)
# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data['temp'].to_list()
# print(len(temp_list))

# print(data['temp'].mean())
# print(data['temp'].max())

# print(data['condition'])
# print(data.condition)

# print(data[data.day=="Monday"])

# print(data[data.temp == data.temp.max()])

# data_dict = {
#     "names":['Ashvik','Souvik','Sudarsh'],
#     "scores":[79,96,68]
# }

# data = pandas.DataFrame(data_dict)
# data.to_csv('new_data.csv')