pin = int(input("Ввведите PIN-код:"))
if (pin // 1000) > 9 or (pin // 1000) == 0:
    print('ERROR')
else:
    a = pin // 1000
    b = (pin % 1000) // 100
    c = ((pin % 1000) % 100) // 10
    d = (((pin % 1000) % 100) % 10)
    if a == b or a == c or a == d or b == c or b == d or c == d:
        print('ERROR')
    else:
        if pin >= 1900 and pin <= 2050:
            print('ERROR')
        else:
            print('OK')
