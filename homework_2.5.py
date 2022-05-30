my_list = [57.8, 46.51, 97, 33.5, 41.07, 31.7, 44.22, 99.09, 74.15, 38]

for i in my_list:
    rub = int(i)
    kop = str(round((i - rub) * 100)).zfill(2)
    print(f'{rub} руб. {kop} коп.')

print(id(my_list))
my_list.sort()
print(id(my_list))
print(my_list)
new_list = my_list.copy()
new_list.reverse()
print(new_list[:5])
print(id(new_list))