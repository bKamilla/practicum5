year = int(input("Введите год:"))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(366)
        else:
            print(365)
    else:
        print(366)
else:
    print(365)
