from time import perf_counter

src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

# for i in range(0, len(src) - 1):
#     if src[i] < src[i + 1]:
#         print(src[i + 1])

start_1 = perf_counter()
result = [src[i + 1] for i in range(len(src) - 1) if src[i] < src[i + 1]]
print(result, type(result), perf_counter() - start_1)

start_2 = perf_counter()
gen_result = (src[i + 1] for i in range(len(src) - 1) if src[i] < src[i + 1])
print([*gen_result], type([*gen_result]), perf_counter() - start_2)
