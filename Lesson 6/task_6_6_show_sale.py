PRICE_BAKERY = "bakery.csv"


def show(argv):
    pos_1 = sys.argv[1:2]
    for pos_1_1 in pos_1:
        pos_1_1 = int(pos_1_1)

    pos_2 = sys.argv[2:]
    for pos_2_2 in pos_2:
        pos_2_2 = int(pos_2_2)

    if not pos_1 and not pos_2:
        with open(PRICE_BAKERY, "r", encoding="utf-8") as show_sale:
            print(*show_sale.readlines())

    if pos_1 and not pos_2:
        with open(PRICE_BAKERY, "r", encoding="utf-8") as show_sale:
            print(*show_sale.readlines()[(pos_1_1 - 1):])

    if pos_1 and pos_2:
        with open(PRICE_BAKERY, "r", encoding="utf-8") as show_sale:
            print(*show_sale.readlines()[(pos_1_1 - 1):pos_2_2])
    return 0


if __name__ == '__main__':
    import sys

exit(show(sys.argv))
