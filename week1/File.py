Name = "TRƯƠNG THÁI TÂN"

def ex11(name):
    if not name:
        return 0
    else:
        Fullname = ""

        Age = input("what's ur age: ")

        Fullname = name + " " + Age + " Tuổi"

    return Fullname

print(ex11(Name))