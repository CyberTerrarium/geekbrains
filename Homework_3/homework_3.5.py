import random


def get_jokes(n, flag = False):
    """
    get_jokes return list with 3 random words from 3 lists for n times
    :param n: int - jokes count
    :param flag: bool - jokes doesnt copy
    :return: list - n jokes
    """
    new_list = []
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

    for i in range(n):
        x, y, z = random.choice(nouns), random.choice(adverbs), random.choice(adjectives)
        s = x + " " + y + " " + z
        new_list.append(s)
        if flag:
            nouns.pop(nouns.index(x))
            adverbs.pop(adverbs.index(y))
            adjectives.pop(adjectives.index(z))
        if len(nouns) == 0 or len(adverbs) == 0 or len(adjectives) == 0:
            new_list.append("Шутки кончились")
            break

    return new_list


print(get_jokes(7, flag=True))
