my_list=['alex', 'sami', 'dave', 'hanna']
nick_name=['al', 'd' , 'ab' , 'ha']


for index in range(0, len(my_list)-1):
    print(f'{my_list[index]} nick name is {nick_name [index]}')


#or
for index, index2 in zip(nick_name, my_list):
    print(f'{my_list[index]} nick name is {nick_name [index2]}')


