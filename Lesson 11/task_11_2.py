class Valid(Exception):
    pass


while True:
    try:
        num_1 = int(input("Введите делитель: "))
        num_2 = int(input("Введите знаменатель: "))
        if num_2 == 0:
            raise Valid("Делить на ноль нельзя!")
        else:
            res = num_1 / num_2
        print(res)
    except ValueError:
        print(f"Введите число")
    except Valid as err:
        print(err)
