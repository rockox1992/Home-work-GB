Num = range(1, 101)
for N in Num:
    if 5 <= N % 10 <= 9 or 0 == N % 10 or 11 <= N <= 14:
        print(N, 'процентов')
    elif 2 <= N % 10 <= 4:
        print(N, 'процента')
    else:
        print(N, 'процент')
