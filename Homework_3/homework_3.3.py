def thesaurus(*args):
    my_dict = {}
    for arg in args:
        my_dict.setdefault(arg[0], []).append(arg)
    return my_dict


workers = thesaurus("Матрёна", "Буженина", "Авдей", "Изя", "Яцек", "Иван", "Баблюба")
print(workers)
