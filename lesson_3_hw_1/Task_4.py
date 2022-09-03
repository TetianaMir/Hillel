mean = input('Введите данные: ').split("*")
name = mean[0]
data_2 = mean[len(mean)-1]
year_2 = data_2[0:4]
data_1 = mean[len(mean)-2]
year_1 = data_1[0:4]
age = (int(year_2) - int(year_1))
print('Name:', name, '\n', 'Age:', age)
