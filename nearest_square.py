import math


def near_sqr(num):
    if num<0:
        print("Please enter number greater than 1")
    elif(num==0):
        print(num, "is a Perfect square")

    elif(num<0.5):
        print("Upper square number>>> 1")
        print("Lower square number>>> 0")
        print("Nearest Square is 0")
    elif(num==0.5):
        print("Upper square number>>> 1")
        print("Lower square number>>> 0")
        print("Its between two square number  0 and 1")

    elif(num<=1):
        print("Upper square number>>> 1")
        print("Lower square number>>> 0")
        print("Nearest Square is 1")
    else:
        p = n = int(num)
        root = math.sqrt(n)
        if int(root) ** 2 == num:
            print(num, "is a Perfect square")
        else:
            while int(root) ** 2 != int(n):
                n += 1
                root = math.sqrt(n)
            else:
                num1 = n
                print("Upper square number>>>" ,num1)
            root = math.sqrt(p)
            while int(root) ** 2 != int(p):
                p -= 1
                root = math.sqrt(p)
            else:
                num2 = p
                print("lower square number>>>" ,num2)
            num3 = num1 - num
            num4 = num - num2
            if num3 < num4:
                print("Nearest Square is >>" ,num1)
            elif num3 == num4:
                print("Its between two square number", num2, "and ", num1)
            else:
                print(num2)
near_sqr(num)
