# ex 01:  vẽ hình tam giác vuông, sử dụng hàm Print

def ex1():
    n = input("Nhap vao so n: ")

    # check for non number input
    while not n.isdigit():
        n = input("Moi nhap lai: ")    

    r = range(int(n + 1))

    for i in r:
        print("*" * i)

#================================================================================================

# ex 02: Write a Python program to calculate the length of a string.

def ex2():
    txt = input("Moi nhap vao van ban: ")

    # check for empty input
    while not txt:
        txt = input("Moi nhap lai: ")
    
    n = len(txt)

    print(f"Van ban co: {n} ky tu")

#================================================================================================

# ex 03: 
# Write a Python program to count the number of characters (character frequency) in a string.
#   Sample String : google.com'
#   Expected Result :   'g': 2, 
#                       'o': 3, 
#                       'l': 1, 
#                       'e': 1, 
#                       '.': 1, 
#                       'c': 1, 
#                       'm': 1

def ex3():
    txt = input("Moi nhap van ban: ")

    while not txt:
        txt = input("Moi nhap lai: ")
    
    TextLength = len(txt)

    hld = {
        "char" : [],
        "Amount" : []
    }

    for i in range(TextLength):
        char = txt[i]
        
        CharIndex = txt.find(char)

        if CharIndex < i:
            continue
        else:
            hld["char"].append(char)            
            hld["Amount"].append(1)

            PreviousIndex = CharIndex
            AmountIndex = len(hld["Amount"]) - 1

            while True:
                CharIndex = txt.find(char, PreviousIndex + 1)
                
                if CharIndex == -1:
                    break
                else:
                    hld["Amount"][AmountIndex] = hld["Amount"][AmountIndex] + 1
                    PreviousIndex = CharIndex

    Amount = hld["Amount"]
    Char = hld["char"]

    for i in range(len(Char)):
        print(f"{Char[i]} : {Amount[i]}")

#================================================================================================

# ex 04: Write a Python program to get a string made of the first 2 and last 2 characters of a given string. If the string length is less than 2, return the empty string instead.
# Sample String : 'w3resource'
# Expected Result : 'w3ce'
# Sample String : 'w3'
# Expected Result : 'w3w3'
# Sample String : ' w'
# Expected Result : Empty String

def ex4():
    txt = input("Moi nhap van ban: ")

    while not txt:
        txt = input("Moi nhap lai: ")

    TextLength = len(txt)

    if TextLength < 2:
        print("Empty String")
    elif TextLength == 2:
        print(txt * 2)
    else:
        print(txt[0] + txt[1] + txt[TextLength - 2] + txt[TextLength - 1])

#================================================================================================

# ex 05: Write a Python program to remove a newline in Python.

def ex5(txt):
    print(txt, end="")

#================================================================================================

# ex 06: Write a Python program to remove existing indentation from all of the lines in a given text.

def ex6(txt):
    print(txt.strip())

#================================================================================================

# ex 07: Write a Python program to reverse a string.

def ex7(txt):
    hld = txt[::-1]
    return hld

#================================================================================================

# ex 08: Write a Python program to count occurrences of a substring in a string.

def ex8(txt):
    hld = txt
    TextLength = len(hld)
    counter = 0

    if not txt:
        return 0
    else:
        for i in range(TextLength):
            counter = counter + round(TextLength / (i + 1))            

        return counter

#================================================================================================

# ex 09: cho 1 chuỗi có sẵn, in ra màn hình chuỗi trong đó các ký tự đc yêu cầu sẽ được thay thế cho các ký tự có sẵn

# đề bài: 
#   - chuỗi đã cho: "Aquafina - Vị ngon của sự tinh khiết"
#   - Yêu cầu: 
#       - ký tự "a" đổi thành "@"
#       - Ký tự "o" đổi thành "0"
#       - Ký tự "s" đổi thành "$"
#       - Ký tự "i" đổi thành "1"


txt = "Aquafina - Vị ngon của sự tinh khiết"

RequirementChange = {
    "a" : "@",
    "o" : "0",
    "s" : "$",
    "i" : "1"
}

def ex9(txt, Changes):
    if not txt:
        return 0
    else:
        hld = txt.lower()

        for i in Changes:
            hld = hld.replace(i, Changes[i])

    return hld

#================================================================================================
# ex 10: Ghép nhiều chuỗi riêng biệt thành 1 chuỗi hoàn chỉnh, ngăn cách bởi dấu cách

 # đề bài:
 #  họ: "Nguyễn "
 #  Tên đệm: "Văn"
 #  Tên: "Tèo"

 #  output: Nguyễn Văn Tèo

Name = {
    "họ" : "Nguyễn",
    "tên đệm" : "Văn",
    "tên" : "Tèo"
}

def ex10(names):
    if not names:
        return 0
    else:
        Fullname = []

        Fullname.append(names["họ"] + " " + names["tên đệm"] + " " + names["tên"])

    return Fullname[0]

#================================================================================================

# ex 11: nhận chuỗi vào là họ và tên, số tuổi của user (dùng hàm input)

#   in ra chuỗi: Họ và tên + số tuổi của user (với họ và tên viết in hoa)

#   ví dụ: "MAI PHƯƠNG THUÝ 39 TUỔI"

def ex11():
    Fullname = input("What's ur name")

    while not Fullname:
        Fullname = input("What's ur name")
        
    Age = input("what's ur age: ")

    Fullname = Fullname + " " + Age + " Tuổi"

    return Fullname



ex4()