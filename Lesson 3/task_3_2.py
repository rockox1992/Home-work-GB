def num_translate_adv(number):
    if number.istitle():
        print(f'"{(dict_eng_ru.get(number.lower())).title()}"')
    else:
        print(f'"{dict_eng_ru.get(number)}"')


dict_eng_ru = {"one": "один", "two": "два", "three": "три", "four": "четыре", "five": "пять",
               "six": "шесть", "seven": "семь", "eight": "восемь", "nine": "девять", "ten": "десять"}

num_translate_adv("Six")
num_translate_adv("nine")
num_translate_adv("Two")
num_translate_adv("eleven")
