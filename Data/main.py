import pandas
# #
# data = pandas.read_csv("weather_data.csv")
# # temp_list = data['temp'].to_list()
# #
# # max = data.temp.max()
# #
# # # average = round(sum(temp_list) / len(temp_list), 2)
# # print(f"Max is {max}")
#
# monday = data[data.day == 'Monday']
# temp = (monday.temp * 1.8) + 32
# print(f"monday temperature in fahrenheit is {temp}")

# dictionary = {
#     'students': ['Jawad', 'Ali', 'Amjad'],
#     'scores': [96, 89, 92]
# }
#
# data = pandas.DataFrame(dictionary)
# data.to_csv('new_data.csv')

data = pandas.read_csv('squirrel_data.csv')
grey_count = len(data[data['Primary Fur Color'] == 'Gray'])
black_count = len(data[data['Primary Fur Color'] == 'Black'])
cinnamon_count = len(data[data['Primary Fur Color'] == 'Cinnamon'])

count_dictionary = {
    'Fur Color': ['black', 'cinnamon', 'gray'],
    'Count': [black_count, cinnamon_count, grey_count]
}

result_data = pandas.DataFrame(count_dictionary)
result_data.to_csv('fur_count.csv')
