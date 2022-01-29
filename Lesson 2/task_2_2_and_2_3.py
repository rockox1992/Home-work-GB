list_task = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

for number in list_task:
    if number.isdigit():
        if int(number) < 10:
            i = list_task.index(number)
            number = f'"0{number}"'
            list_task.pop(i)
            list_task.insert(i, number)
        else:
            i = list_task.index(number)
            number = f'"{number}"'
            list_task.pop(i)
            list_task.insert(i, number)

    elif number.startswith('+'):
        if int(number) < 10:
            i = list_task.index(number)
            number = f'"+0{number[1:]}"'
            list_task.pop(i)
            list_task.insert(i, number)

    elif number.startswith('-'):
        if int(number) < 10:
            i = list_task.index(number)
            number = f'"-0{number[1:]}"'
            list_task.pop(i)
            list_task.insert(i, number)
print(*list_task)
