#calculator

while True:
    a = int (input(" num1: "))
    b = int (input(" num2: "))
    c = int(input("your operator: 1.plus, 2.mines, 3.divide, 4.time "))

    if c == 1:
        print(a+b)
    elif c == 2 :
        print(a-b)
    elif c == 3 :
        print(a/b)
    elif c == 4 :
        print(a*b)
else:
    print("operator number can be between 1 to 4")
    
