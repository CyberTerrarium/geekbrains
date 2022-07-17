def thesaurus_adv(*args):
    my_dict = {}
    for s_n in args:
        my_dict.setdefault(s_n.split()[1][0], {}).setdefault(s_n.split()[0][0], []).append(s_n)
    return my_dict

workers = thesaurus_adv("Матрёна Костюшова", "Буженина Коровина", "Авдей Смутьянов", "Изя Гольберштейн",
                        "Яцек Бонифасский", "Иван Твердолобов", "Баблюба Тетина", "Мурка Кошкина", "Яша Баша")
print(workers)
