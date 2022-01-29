def odd_nums(n):
    for num in range(1, n + 1, 2):
        yield num**2


odd_to_15 = odd_nums(15)
print(next(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))
