def num_translate(number):
    print(f'"{dict_eng_ru.get(number)}"')


dict_eng_ru = {"one": "один", "two": "два", "three": "три", "four": "четыре", "five": "пять",
               "six": "шесть", "seven": "семь", "eight": "восемь", "nine": "девять", "ten": "десять"}

num_translate("six")
num_translate("nine")
num_translate("two")
num_translate("eleven")
