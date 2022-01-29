d_list = [400153, 53, 153, 4153, 777, 555, 789, 87, 700000000, 3600, 60, 86400]

for duration in d_list:
    duration_d = duration // 86400
    duration_h = duration // 3600 % 24
    duration_m = duration // 60 % 60
    duration_s = duration % 60
    if duration < 60:
        print('{} сек'.format(duration_s))
    elif duration < 3600:
        print('{} мин {} сек'.format(duration_m, duration_s))
    elif duration < 3600 * 24:
        print('{} час {} мин {} сек'.format(duration_h, duration_m, duration_s))
    else:
        print('{} дн {} час {} мин {} сек'.format(duration_d, duration_h, duration_m, duration_s))
