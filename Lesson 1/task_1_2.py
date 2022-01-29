num = range(1, 1001)
odd_cubed = []
sum_num_list = []
sum_num = 0
sum_num_list_17 = []
sum_num_17 = 0

for i in num:
    if not i % 2 == 0:
        odd_cubed.append(i ** 3)
#print('odd_cubed', odd_cubed)


for odd in odd_cubed:
    ind = 0
    a = odd
    while odd != 0:
        ind += odd % 10
        odd //= 10
    if ind % 7 == 0:
        sum_num_list.append(odd_cubed[odd_cubed.index(a)])
    ind = 0
#print('sum_num_list', sum_num_list)

for sum_n in sum_num_list:
    sum_num += sum_n
print('sum_num', sum_num)


for i_17, item in enumerate(odd_cubed):
    odd_cubed[i_17] = item + 17
#print('odd_cubed_17', odd_cubed)


for odd in odd_cubed:
    ind_17 = 0
    b = odd
    while odd != 0:
        ind_17 += odd % 10
        odd //= 10
    if ind_17 % 7 == 0:
        sum_num_list_17.append(odd_cubed[odd_cubed.index(b)])
    ind_17 = 0
#print('sum_num_list_17', sum_num_list_17)

for sum_17 in sum_num_list_17:
    sum_num_17 += sum_17
print('sum_num_17', sum_num_17)


