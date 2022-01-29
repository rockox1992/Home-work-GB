price = [0.07, 0.13, 10.09, 51.62, 88.66, 35.98, 3.05, 40.12, 3.45, 36.37, 68.62, 73.45, 12.11, 20.45, 68.61, 45.26]
print(id(price))
price_C = []

for i in price:
    R_r = int(i % 100 // 10)
    r_R = int(i % 10)
    K_k = int(i * 10 % 10)
    k_K = int(round(i * 100) % 10)
    print(f'{R_r}{r_R} руб {K_k}{k_K} коп,', end=' ')
print('\n')

price.sort()

for i in price:
    R_r = int(i % 100 // 10)
    r_R = int(i % 10)
    K_k = int(i * 10 % 10)
    k_K = int(round(i * 100) % 10)
    print(f'{R_r}{r_R} руб {K_k}{k_K} коп,', end=' ')
print('\n')

print(id(price))

price = sorted(price, reverse=True)
for i in price:
    R_r = int(i % 100 // 10)
    r_R = int(i % 10)
    K_k = int(i * 10 % 10)
    k_K = int(round(i * 100) % 10)
    print(f'{R_r}{r_R} руб {K_k}{k_K} коп,', end=' ')
    price_C.append(f'{R_r}{r_R} руб {K_k}{k_K} коп,')
print('\n')
print(*price_C[:5])
