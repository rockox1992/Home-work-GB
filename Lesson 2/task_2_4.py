task_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй',
             'директор аэлита']

count = 0
while count < len(task_list):
    test = task_list[count]
    count += 1
    print('Привет, ', (test.split(' ')[-1]).capitalize(), '!', sep='')
