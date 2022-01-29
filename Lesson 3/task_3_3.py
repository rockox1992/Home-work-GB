def thesaurus(args):
    dict_names = {}
    for name in args:
        first_letter_name = name[0]
        dict_names[first_letter_name] = dict_names.get(first_letter_name, []) + [name]
    return print(sorted(dict_names.items()))


names = ["Иван", "Мария", "Петр", "Илья", "Константин"]

thesaurus(names)
