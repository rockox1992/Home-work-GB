import json
import codecs


def group(users="./users_6_3.csv",
          hobby="./hobby_6_3.csv"):
    fio_list = []
    hob_list = []
    with open(users, 'r', encoding='utf-8') as users_file:
        a = users_file.readlines()
        for fio in a:
            fio = fio.replace("\ufeff", "")
            fio = fio.replace("\n", "")
            fio_list.append(fio)
    with open(hobby, 'r', encoding='utf-8') as hobby_file:
        b = hobby_file.readlines()
        for hob in b:
            hob = hob.replace("\ufeff", "")
            hob = hob.replace("\n", "")
            hob_list.append(hob)
    if len(fio_list) > len(hob_list):
        hob_list.append(None)
    if len(fio_list) < len(hob_list):
        return 1
    dict_names = list(zip(fio_list, hob_list))
    with codecs.open('out_6_3.txt', 'w', encoding='utf-8') as f:
        json.dump(dict_names, f, ensure_ascii=False)


print(group())
