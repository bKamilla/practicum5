n = int(input("Введите кол-во кнатов:"))
a = n // 29
b = a // 17
knati = n % 29
sikli = a % 17
galleoni = b
if sikli == 0 and galleoni == 0 and knati != 0:
    print(knati,'кнатов')
elif sikli == 0 and knati == 0 and galleoni != 0:
    print(galleoni,'галлеонов')
elif galleoni == 0 and knati ==0 and sikli != 0:
    print(sikli,'сиклей')
elif galleoni == 0 and (sikli != 0 and knati != 0):
    print(sikli,'сиклей')
    print(knati,'кнатов')
elif sikli == 0 and (galleoni != 0 and knati != 0):
    print(galleoni,'галлеонов')
    print(knati,'кнатов')
elif knati == 0 and (galleoni != 0 and sikli != 0):
    print(galleoni,'галлеонов')
    print(sikli,'сиклей')
else:
    print(galleoni,'галлеонов')
    print(sikli,'сиклей')
    print(knati,'кнатов')

