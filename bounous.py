length=int(input("enter the size for your list: "))
mylist=[]

for index in range(0, length):
    mylist[index] = input("enter the lists: ")


max=mylist[0];

for index in range(0, length):
     if max< mylist[index]:
         max=mylist[index]
         print("the max is: " , max)