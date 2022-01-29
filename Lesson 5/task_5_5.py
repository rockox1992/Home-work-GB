src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

src_set = set()
tmp = set()

for el in src:
    if el not in tmp:
        src_set.add(el)
    else:
        src_set.discard(el)
    tmp.add(el)
number_list = [el for el in src if el in src_set]
print(number_list)
