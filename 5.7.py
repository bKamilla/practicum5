n, k, m = map(int, input().split())
if k < m:
    f1 = k - 1 + n - m
    f2 = m - k - 1
    if f1 <= f2:
        print(f1)
    else:
        print(f2)
if k > m:
    f1 = n - k + m - 1
    f2 = k - m - 1
    if f1 <= f2:
        print(f1)
    else:
        print(f2)
if k == m:
    print(0)
