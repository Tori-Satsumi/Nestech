# =====================================================================================
"""
Ghép nhiều chuỗi riêng biệt thành 1 chuỗi hoàn chỉnh, ngăn cách bởi dấu cách, sử dụng hàm Join()

đề bài:
    họ: "Nguyễn "
    Tên đệm: "Văn"
    Tên: "Tèo"

    output: Nguyễn Văn Tèo
"""

def ex1():
    name = ("Nguyễn", "Văn", "Tèo")
    Fullname = " ".join(name)
    print(Fullname)

# =====================================================================================
"""
Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old
extra: Depending on whether the number is even or odd, print out an appropriate message to the user ("your age is odd/even")
"""

def ex2():
    try:
        Name = input("What's your name? ")
        if not Name:
            print("Invalid input")
            return 0
        
        Age = input("How old are you? ")
        Age = int(Age)

    except:
        print("Invalid input")
    else:
        if Age < 100:
            print(f"\n{Name} will turn 100 in {100 - Age}")
        else:
            print(f"\n{Name} is above 100 years old!")

        print("Your age is an ", end="")
        if not Age % 2:
            print("even number\n")
        else:
            print("odd number\n")

# =====================================================================================
"""
Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)

example: 
    - anna
    - civic
    - level
    - madam
    - mom
    - noon
    - radar
    - wow

"""

def ex3():
    txt = input("\nInput a string value: ")

    if not txt:
        print("Invalid input")
        return 0
    
    hld = txt[::-1]

    print("This string is ", end="")
    if hld.lower() == txt.lower():
        print("a palindrome\n")
    else:
        print("not a palindrome\n")

# =====================================================================================
"""
write a program, and returns the largest number of two number. Do this without using the Python max() function!
a = 3
c = 5
print(f"max = {c})
"""

def ex4():
    try:
        num1 = input("num 1: ")
        num1  = float(num1)

        num2 = input("num 2: ")
        num2  = float(num2)
    
    except:
        print("Invalid input")

    else:    
        if num1 > num2:
            print("num 1 is the largest")
        elif num1 == num2:
            print("num 1 is equal to num2")
        else:
            print("num 2 is the largest")

# =====================================================================================
"""
write a program, and returns the largest number of three number. Do this without using the Python max() function!
a = 3
b = 4
c = 5
print(f"max = {c})
"""

def ex5():
    NumList = []
    print()
    
    for i in range(3):
        try:
            hld = input(f"num {i + 1}: ")
            hld = float(hld)
        except:
            print("Invalid input")
            return 0
        else:        
            NumList.append(hld)

    Lnum = NumList[0]

    for i in NumList[1:]:
        if i > Lnum:
            Lnum = i

    print(f"\nLargest number: {Lnum} \n")
