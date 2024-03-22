weightf = int(input("Введите вес:"))
heightd = int(input("Введите рост:"))
heightm = 0.0254 * heightd
weightkg = weightf * 0.453592
IMT = weightkg / (heightm * heightm)

if IMT < 16:
    print('выраженный дефицит массы тела')
elif 16 <= IMT <= 18.49:
    print('недостаточная масса тела')
elif 18.5 <= IMT <= 24.99:
    print('норма')
elif 25 <= IMT <= 29.99:
    print('избыточная масса тела')
elif 30 <= IMT <= 34.99:
    print('ожирение первой степени')
elif 35 <= IMT <= 39.99:
    print('ожирение второй степени')
else:
    print('ожирение третьей степени')

