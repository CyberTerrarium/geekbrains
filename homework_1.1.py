duration = 11153

if duration < 60:
    print(duration, 'секунд')
elif duration < 3600:
    print(f'{duration // 60} минут {duration % 60} секунд')
elif duration < 86400:
    print(f'{duration // 3600} часов {duration % 3600 // 60} минут {duration % 60} секунд')
else:
    print(f'{duration // 86400} дней {duration // 3600 % 24} часов {duration % 3600 // 60} минут {duration % 60} секунд')