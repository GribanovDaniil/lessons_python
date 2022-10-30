a_input = ('rus', 'eng', 'jap', 'rus', 'eng')
a_set = set(a_input)
a_list list(a_set)
print(a_list == a_input)
for i in a_input:
    if i in a_input:
        a = list.remove(i)
print(a_input)