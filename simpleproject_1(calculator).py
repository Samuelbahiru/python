# calculator 
print(" Press 1 for addition ")
print(" Press 2 for substraction  ")
print(" Press 3 for product ")
print(" Press 4 for division ")

choice=input()
if int(choice)==1:
    number_1= int(input("enter the first number: "))
    number_2 = int(input("enter the second number: "))
    sum=number_1 + number_2
    print(f'the sum of {number_1} and {number_2} is {sum}')
elif int(choice)==2:
    number_1= int(input("enter the first number: "))
    number_2 = int(input("enter the second number: "))
    sub=number_1 - number_2
    print(f'the difference of {number_1} and {number_2} is {sub}')
elif int(choice)==3:
    number_1= int(input("enter the first number: "))
    number_2 = int(input("enter the second number: "))
    pro=number_1 * number_2
    print(f'the prduct of {number_1} and {number_2} is {pro}')
elif int(choice)==4:
    number_1= int(input("enter the first number: "))
    number_2 = int(input("enter the second number: "))
    div=number_1 / number_2
    print(f'the division of {number_1} and {number_2} is {div}')
else: 
    pass