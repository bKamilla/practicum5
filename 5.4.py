a = int(input("Введите количество попугаев,не превыщающее 100:"))
if a % 10 == 1 and a != 11:
    print(a, 'попугай')
elif (a % 10 == 2 or a % 10 == 3 or a % 10 == 4) and ( a != 12 and a != 13 and a != 14):
    print(a, 'попугая')
else:
    print(a, 'попугаев')

