#to do list

from datetime import datetime
current_datetime = datetime.now()

l = []
while True:
    a = int(input("1.do list , 2.date and time , 3.exit "))

    if a == 1 :
        b = int(input("1.add , 2.remove"))

        if b == 1:
            plan = input("enter your plan for add:  ")
            l.append(plan)
        elif b == 2 :
            plan = input("enter your plan for remove: ")
            l.remove(plan)
        else:
            print(" that's incorrect! ")

    elif a == 2:
        print("Current date and time:", current_datetime)
    elif a == 3:
        break
    else :
        print(" that's incorrect! ")
        break
for i , plan in enumerate (l):
    print(str (i+1) + '.' , plan)