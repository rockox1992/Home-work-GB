odd_to = 3
gen_nums = (num**2 for num in range(1, odd_to + 1, 2))

print(next(gen_nums))
print(next(gen_nums))
print(next(gen_nums))
