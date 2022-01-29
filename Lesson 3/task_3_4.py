def thesaurus_adv(args):
    namelist = list(map(str, args))
    dict_surnames = {}
    dict_main = {}
    for name in namelist:
        surname = name.split(' ')[-1].title()
        first_letter_surname = surname[0]
        dict_surnames[first_letter_surname] = dict_surnames.get(first_letter_surname, []) + [name]
    for namelist in dict_surnames.values():
        dict_names = {}
        for name in namelist:
            surname = name.split(' ')[-1].title()
            first_letter_surname = surname[0]
            first_letter_name = name[0]
            dict_names[first_letter_name] = sorted(dict_names.get(first_letter_name, []) + [name])
            dict_main[first_letter_surname] = dict_main.get(first_letter_surname, dict_names)
    return print(dict(sorted(dict_main.items())))


name_surname = ("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")

thesaurus_adv(name_surname)
