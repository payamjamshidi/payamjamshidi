#stoqumetry

while True:
    a = int (input(" your hight to cm: "))
    b = int(input("your operator: 1.metr, 2.inch: "))

    if a <= 150 or a >= 210:
        print("hight <= 150 or hight >= 210")

    elif b == 1:
        print(a/100 , "metr")

    elif b == 2:
        print(a/2.5 , "inch")

    elif b != 1 or b!=2:
        print("1 or 2")