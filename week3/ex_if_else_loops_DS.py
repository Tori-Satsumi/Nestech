import copy
from random import randrange
import datetime
import os
import calendar 
from string import punctuation

# =============================================================
"""
problems: trong sample có bao nhiêu phần tử là số chẵn?
"""

def ex1():

    sample = [
        100,
        "chín mươi tám",
        "vợ chồng A Phủ",
        9999,
        [10, 99, 54, 2, -3],
        -1, 
        "Nghìn chín"
    ]

    def loope(lst = sample):

        cnt = 0
        for index in range(len(lst)):
            hld = ""
            lstCheck = False        
            try:
                hld = float(lst[index])
            except:
                _i = type(lst[index])

                if _i == list or _i == set:
                    hld = lst[index]
                    lstCheck = True            
                else:
                    continue
                
            if not lstCheck: 
                if not hld % 2:
                    cnt += 1
            else:
                cnt += loope(hld)

        return cnt

# =============================================================
"""
problems: list con nằm trong sample có bao nhiêu phần tử là số chẵn?
"""

def ex2():
    sample = [
        "Ronaldo", 
        "Shin - Cậu bé bút chì", 
        1996, 
        "Ráp Việt mùa 3", 
        [100, 2, 5, 7, 99, 
            [
                1, 2, 3,
                [
                    "hehe", "hihi"
                ]
            ]
        ], 
        "Trời mưa sấm chớp bão bùng - Cho hỏi đêm nay nàng cùng với ai?",
        "Vợ Nhặt"
    ]

    def loope(lst = sample):
        cnt = 0
        for index in range(len(lst)):
            _i = type(lst[index])
            
            if _i == list or _i == set:
                cnt += (1 + loope(lst[index]))

        return cnt


    print(loope())
# =============================================================
"""
write a program that swap first and last element of a list
"""

def ex3():
    lst = [
        1, 2, 3, 4, 5
    ]

    def swap(lst):
        if not type(lst) == list:
            return None
        
        hld = copy.deepcopy(lst)
        # hld = lst

        itemhld = hld[0]

        hld[0] = hld[len(hld) - 1]
        hld[len(hld) - 1] = itemhld

        return hld

    tst = swap(lst)
    print(tst)
    print(lst)

# =============================================================
"""
: vẽ hình tam giác vuông, 
    - sử dụng hàm Print
    - Sử dụng vòng lặp for
    - Sử dụng vòng lặp while
    - yêu cầu viết bằng function, với số dòng được truyền vào (nếu đã biết làm, còn ko biết làm thì thôi bỏ qua cũng ko sao)
ví dụ:

*
**
***
****
*****
******

"""

def ex4(amount):
    _i = type(amount)
    if _i == int or _i == float:
        ...
    else:
        return ""

    if amount == 0:
        return ""

    print()
    for i in range(amount):
        print("*" * (i + 1))

    print()

# =============================================================
"""
cho dãy số từ 1 đến 100
in ra các số thoả mãn điều kiện:
    - chia hết cho 2
    - chia hết cho 3
    - (chia hết cho cả 2 và 3)

expected output: 
    - các số chia hết cho 2: 2,4,6,8.....
    - các số chia hết cho 3: 3,6,9.....
    - các số chia hết cho cả 2 và 3: 6,12,18.....
"""

def ex5():
    lstofnumdiv2 = []
    lstofnumdiv3 = []
    lstofnumdiv6 = []

    for i in range(1, 101):
        if not i % 2:
            lstofnumdiv2.append(i)
        elif not i % 3:
            lstofnumdiv3.append(i)
        
        if not i % 6:
            lstofnumdiv6.append(i)

    print(f"\nCác số chia hết cho 2: {lstofnumdiv2}\n")
    print(f"\nCác số chia hết cho 3: {lstofnumdiv3}\n")
    print(f"\nCác số chia hết cho 6: {lstofnumdiv6}\n")

# =============================================================
"""
cho chuỗi: list_input = [1,2,3,4,5,6,7,8]
in ra chuỗi mới với mỗi phần tử của chuỗi mới là bình Phương của phần tử tương ứng trong chuỗi cũ
expected_output = [1,4,9,16,25,36,49,64]
"""

def ex6():
    list_input = [1,2,3,4,5,6,7,8]

    def squareofitem(lst):
        hld = copy.deepcopy(lst)

        for index in range(len(hld)):
            hld[index] = hld[index] ** 2

        return hld

    lst = squareofitem(list_input)
    print(lst)

# =============================================================
"""
cho 3 số tự nhiên
sắp xếp các số tự nhiên theo thứ tự tăng dần

bonus: áp dụng tương tự với 4 số
bonus 2: phát triển thành thuật toán, có thể sắp xếp được n số (cái này khó, làm đc thì làm, ko làm được thì bỏ qua)
Hint: search google về thuật toán sắp xếp
"""

def ex7():

    def sort(lst):
        if not lst and not type(lst) == list:
            return None

        SortedLst = copy.deepcopy(lst)

        while True:        
            Unchange = True
            for i in range(len(SortedLst) - 1):
                if SortedLst[i] > SortedLst[i + 1]:
                    Unchange = False
                    hld = SortedLst[i]
                    SortedLst[i] = SortedLst[i + 1]
                    SortedLst[i + 1] = hld
            
            if Unchange:
                break
        
        return SortedLst

    def randomgenlst():
        ln = randrange(10, 101)
        lst = []
        for i in range(ln):
            lst.append(randrange(1, 101))

        return lst    

    ranlist = randomgenlst()

    print(sort(ranlist))

# =============================================================
"""
display the current date and time.
"""

def ex8():
    x = datetime.datetime.now()

    print(f"today is: {x.strftime("%x")} and it is {x.strftime("%X")}")

# =============================================================
"""
Write a Python program that accepts a filename from the user and prints the extension of the file.
"""


def ex9():
    filename = input("\nwhat is the file name: ")

    # find the file path in the user desktop
    for root, dirs, files in os.walk("C:\\Users\\PC\\Desktop\\"):
        for name in files:
            if name == filename:
                print(os.path.abspath(os.path.join(root, name)))

    print()

# =============================================================
"""
Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
Sample value of n is 5
Expected Result : 615
"""

def ex10():
    num = input("What's your number: ")

    try:
        int(num)
    except:
        return None

    sm = 0
    for i in range(3):
        hld = str(num) + str(abs(int(num))) * i
        sm += int(hld) 

    print(sm)

# =============================================================
"""
prints the calendar for a given month and year.
Note : Use 'calendar' module.
"""

def ex11():
    yy = input("\nWhat's the year: ")
    mm = input("\nWhat's the month: ")
    
    try:
        yy = int(yy)
        mm = int(mm)
    except:
        return None
    
    print()
    print(calendar.month(yy, mm)) 

# =============================================================
"""
returns a list that contains only the elements that are common between 2 lists (without duplicates). Make sure your program works on two lists of different sizes.
example:
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
"""

def ex12():
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

    cpy1 = []
    cpy2 = []
    if len(a) < len(b):
        cpy1 = copy.deepcopy(a)
        cpy2 = copy.deepcopy(b)
    else:
        cpy1 = copy.deepcopy(b)
        cpy2 = copy.deepcopy(a)

    hld = []

    for i in range(len(cpy1)):
        if cpy1[i] in cpy2 and not cpy1[i] in hld:
            hld.append(cpy1[i])

    print(hld)

# =============================================================
"""
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]. Write one line of Python that takes this list a and makes a new list that has only the even elements of this list in it."

hint: use list comprehension
"""

def ex13():
    def randomgenlst():
        ln = randrange(10, 101)
        lst = []
        for i in range(ln):
            lst.append(randrange(1, 101))

        return lst    
    
    a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    b = randomgenlst()

    trsh = []
    def add(item):
        trsh.append(item)
        return item

    hld = copy.deepcopy(b)

    EvenNumLst = [add(hld[index]) for index in range(len(hld)) for num in range(2, hld[index]) if not hld[index] % num and not hld[index] in trsh]

    print(hld)
    print(EvenNumLst)


# =============================================================
"""
Ask the user for a number and determine whether the number is prime or not. (a prime number is a number that has no divisors.
"""

def ex14():
    UserNum = input("what's you num in mind: ")
    
    try:
        UserNum = int(UserNum)
    except:
        print("Invalid input")
        return None
    
    for num in range(2, UserNum):
        if not UserNum % num:
            print("The input num is Not Prime number")
            return False
        
    print("The input num is Prime number")
    return True


# =============================================================
"""
Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.
"""

def ex15():
    Rannum = randrange(1, 10)
    
    UserNum = input("what's you num in mind(1-9): ")
    
    try:
        UserNum = int(UserNum)
    except:
        print("Invalid input")
        return None

    if UserNum < 1 or UserNum > 9:
        print("Input out of bound")
        return None
         
    if UserNum < Rannum:
        print("too low")
    elif UserNum > Rannum:
        print("too high")
    else:
        print("Correct guess")


# =============================================================
"""
Write a password generator in Python. Be creative with how you generate passwords - strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols. The passwords should be random, generating a new password every time the user asks for a new password
"""
def ex16():
    passlen = randrange(6, 13)

    specialchar = punctuation
    uplet = list(map(chr, range(65, 91)))
    lowlet = list(map(chr, range(97, 123)))

    password = ""

    letcheck = False
    numcheck = False
    charcheck = False
    
    while True:
        for i in range(passlen):
            chances = randrange(0, 100)
            rannum = randrange(0, 101)

            if chances >= 20:
                _p = randrange(0, 2)
                if _p:
                    password = password + str(uplet[randrange(0, 26)])
                else:
                    password = password + str(lowlet[randrange(0, 26)])
                
                letcheck = True

            elif chances >= 5:
                password = password + str(rannum)
                numcheck = True

            else:
                password = password + str(specialchar[randrange(0, len(specialchar))])
                charcheck = True

        if letcheck and numcheck and charcheck:
            break
        else:
            password = ""
            letcheck = False
            numcheck = False
            charcheck = False

    print()
    print(password)
    print()
    return password

# =============================================================

