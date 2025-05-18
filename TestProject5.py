#contact

mydic = {}

while True:

    a = int(input("1.add , 2.remove , 3.search , 4.exit: "))
    if a == 1:
        name = input("name: ")
        phone = int(input("phone: "))
        mydic[name] = phone
    
    elif a == 2:
        key_to_delete = input("put name you want to delete:  ")
        
        if key_to_delete in mydic:
            del mydic[key_to_delete]
            print(f"key'{key_to_delete}'deleted")
        else:
            print(f"key'{key_to_delete}' dosen't exist!")
    
    elif a == 3:
        search = input("name: ")
        if search in mydic:
            print(f"search phone is: {mydic[search]}" )
    
    elif a == 4:
       break
    
    else:
        print(" only .1 .2 .3 .4 could be accepted!")

for i , a in enumerate (mydic):
    print(str (i+1) + '.' , name , '-' , phone)