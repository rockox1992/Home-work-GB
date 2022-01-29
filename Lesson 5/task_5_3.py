tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена', 'Константин', 'ИИИигорь', 'Валера']
sh_classes = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']

for sh in sh_classes:
    if len(tutors) > len(sh_classes):
        sh_classes.append('None')

gen_list_tutors = (name for name in tutors)
gen_list_sh = (cls for cls in sh_classes)

print(type(gen_list_tutors), type(gen_list_sh))
print(next(gen_list_tutors), ', ', next(gen_list_sh), sep='')
print(next(gen_list_tutors), ', ', next(gen_list_sh), sep='')
print(next(gen_list_tutors), ', ', next(gen_list_sh), sep='')
print(next(gen_list_tutors), ', ', next(gen_list_sh), sep='')
print(next(gen_list_tutors), ', ', next(gen_list_sh), sep='')
print(next(gen_list_tutors), ', ', next(gen_list_sh), sep='')
print(next(gen_list_tutors), ', ', next(gen_list_sh), sep='')
print(next(gen_list_tutors), ', ', next(gen_list_sh), sep='')
print(next(gen_list_tutors), ', ', next(gen_list_sh), sep='')
print(next(gen_list_tutors), ', ', next(gen_list_sh), sep='')
print(type(gen_list_tutors), type(gen_list_sh))
