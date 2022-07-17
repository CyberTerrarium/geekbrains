translations = {'zero': 'ноль', 'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять',
                'six': 'шесть', 'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}


def num_translate_adv(word):
    if word.lower() in translations:
        if word[0] in "FSENZOT":
            return translations.get(word.lower()).capitalize()
    return translations.get(word)


print(num_translate_adv("Seven"))