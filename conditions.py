name=input("Enter your name: ")
age=input("Enter your age: ")

if int(age)>=18:
    print(f'Your ID is processed please wait for a secound ...')
elif int(age)==16:
    print(f'Your need to get 18 years old to get your ID, please came back after 2 years')
elif int(age)==14:
    print(f'Your need to get 18 years old to get your ID, please came back after 4 years')
elif int(age)==12:
    print(f'Your need to get 18 years old to get your ID, please came back after 6 years')
elif int(age)==10:
    print(f'Your need to get 18 years old to get your ID, please came back after 8 years')
elif int(age)==8:
    print(f'Your need to get 18 years old to get your ID, please came back after 10 years')
else:
    print(f'Your need to get 18 years old to get your ID')



