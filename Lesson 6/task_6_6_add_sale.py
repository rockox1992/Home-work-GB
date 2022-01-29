PRICE_BAKERY = "bakery.csv"


def main(argv):
    with open(PRICE_BAKERY, "a", encoding="utf-8") as bakery:
        bakery.writelines("%s\n" % line for line in argv[1:])
    return 0


if __name__ == '__main__':
    import sys

exit(main(sys.argv))
