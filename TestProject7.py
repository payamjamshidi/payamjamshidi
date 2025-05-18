#libraray

class Books:
    def __init__(self, name ,auther , PublicYear):
        self.name = name
        self.auther = auther
        self.PublicYear = PublicYear

    def __str__(self):
        return(f"{self.name},{self.auther},{self.PublicYear}")

libarary = []

while True:
    member = int(input("\n1.add book ,\n2. list item, \n3.remove ,\n4.exit \n"))
    if member == 1:
        Name = input("\n name:")
        Auther = input("\n Auther:")
        PublicYear = input("\n PublicYear:")
    
        book = Books( Name , Auther , PublicYear)
        libarary.append(book)

    if member == 2:
        for i , book in enumerate(libarary):
            print(str (i+1) + '.' , book)

    if member == 3:
        
        for index , book in enumerate(libarary):
            print(f"{index +1}. {book}")
        try:    
            Num = int(input("\n book number you want ti remove:"))
            if 0 <= Num < len(libarary):
                removed_book = libarary.pop(Num-1)
                print("deleted")
            else:
                print("not found!")

        except ValueError:
            print("\n book number you want ti remove")
    if member == 4:
        print("have a nice day! ")
        break

