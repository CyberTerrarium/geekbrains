my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
total = ""

for i in range(len(my_list)):
    if my_list[i][-1].isdigit():
        if int(my_list[i]) < 10:
            my_list[i] = my_list[i].replace(my_list[i][-1], my_list[i][-1].zfill(2))
        my_list[i] = f'"{my_list[i]}"'
    total += my_list[i] + " "

print(total.rstrip())
