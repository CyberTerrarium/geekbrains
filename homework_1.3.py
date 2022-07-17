for i in range (0, 101):
    if 9 < i < 21:
        print(i, "процентов")
    elif i % 10 == 0:
        print(i, "процентов")
    elif i % 10 == 1:
        print(i, "процент")
    elif 1 < i % 10 <5:
        print(i, "процента")
    else:
        print(i, "процентов")