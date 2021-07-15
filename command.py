i=0
list=[]
while i<=5:
    command=(input("enter command"))
    splitcommand=command.split()
    if splitcommand[0]=="append":
        list.append(int(splitcommand[1]))
        print(list)
    elif splitcommand[0]=="insert":
        list.insert(int(splitcommand[1],int(splitcommand[2])))
        print(list)
    elif splitcommand[0]=="sort":
        list.sort()
        print(list)
    elif splitcommand[0]=="reverse":
        list.reverse
        print(list)
    elif splitcommand[0]=="pop":
         list.pop()
         print(list)
    else:
        print("your choice is done")