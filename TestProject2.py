#guess_number

while True:
    a = int(input("num bitwen 1 , 10: "))

    import random
    b = random.randrange(1, 10)
    print(b)

    if a == b:
        print("you win")
    elif a > 10 or a < 0:
        print("can't be more than 10 or less than 0")
    else:
        print ("you lose")
    