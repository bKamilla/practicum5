a = int(input("Введите количество подданых,которые видели улыбку в 1 день:"))
b = int(input("Введите количество подданых,которые видели улыбку во 2 день:"))
c = int(input("Введите количество подданых,которые видели улыбку в 3 день:"))
k = 0
if a == b or a == c or b == c:
    k = 2
if a == b == c:
    k = 3
print(k)
