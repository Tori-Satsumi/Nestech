import math

Pi = math.pi

# =====================================================================================
"""
Write a Python program to calculate the area of a trapezoid (hình thang)
Note : A trapezoid is a quadrilateral with two sides parallel. The trapezoid is equivalent to the British definition of the trapezium. An isosceles trapezoid is a trapezoid in which the base angles are equal so.
Test Data:
Height : 5
Base, first value : 5
Base, second value : 6
Expected Output: Area is : 27.5
"""

def ex1():
    try:
        Height = input("Height: ")
        Height = float(Height)

        Base1 = input("Base, first value: ")
        Base1 = float(Base1)

        Base2 = input("Base, second value: ")
        Base2 = float(Base2)
        
    except:
        print("Input value invalid")

    else:
        Area = ((Base1 + Base2) / 2) * Height
        print(Area)

# =====================================================================================
"""
Write a Python program to calculate the surface volume and area of a cylinder.
Note: A cylinder is one of the most basic curvilinear geometric shapes, the surface formed by the points at a fixed distance from a given straight line, the axis of the cylinder.
Test Data:
volume : Height (4), Radius(6)
Expected Output:
Volume is : 452.57142857142856
Surface Area is : 377.1428571428571

"""

def ex2():
    try:
        Height = input("Height: ")
        Height = float(Height)

        Radius = input("Radius: ")
        Radius = float(Radius)

    except:
        print("Input value invalid")

    else:
        Area = 2 * Pi * Radius * (Height + Radius)
        Volumn = Pi * Height * (Radius ** 2)

        print(f"\nVolumn is: {Volumn}")
        print(f"Area is: {Area}\n")

# =====================================================================================
"""
Write a Python program to calculate the surface volume and area of a sphere.
Note: A sphere is a perfectly round geometrical object in three-dimensional space that is the surface of a completely round ball.
Test Data:
Radius of sphere : .75
Expected Output :
Surface Area is : 7.071428571428571
Volume is : 1.7678571428571428
"""

def ex3():
    Radius = input("Radius of sphere: ")

    try:
        Radius = float(Radius)

    except:
        print("Input value invalid")

    else:
        Area = 4 * Pi * (Radius ** 2)
        Volumn = (4 / 3) * Pi * (Radius ** 3)

        print(f"\nSurface Area is: {Area}")
        print(f"Volumn is: {Volumn}\n")

# =====================================================================================
"""
additional: hình chữ nhật, hình tròn, hình tam giác,...
biết rằng đã có đủ các tham số cần thiết
"""
    
# =====================================================================================
'''
chuyển đổi từ độ C sang độ F và ngược lại
'''

def ex4():
    Mode = input("\nCelsius to Fahrenheit : 1\nFahrenheit to Celsius : 2\nMode: ")

    try:
        Mode = int(Mode)

    except:
        print("Invalid mode")

    else:        
        try:
            if Mode == 1:
                Cel = input("Celsius: ")
                Cel = float(Cel)
                Fah = Cel * (9 / 5) + 32
                print(f"Fahrenheit: {Fah}")

            elif Mode == 2:
                Fah = input("Fahrenheit: ")
                Fah = float(Fah)
                Cel = (Fah - 32) * 5 / 9
                print(f"Celsius: {Cel}")

            else:
                print("Invalid mode")
                return 0
            
        except:
            print("Invalid input")

# =====================================================================================
"""
chuyển đổi vận tốc từ Km/h sang Mph
áp dụng: tính vận tốc. cho các tham số về quãng đường và thời gian
"""

def ex5():
    KmhtoMphConst = 0.621371192

    try:
        Dist = input("Distances (km): ")
        Dist = float(Dist)

        Time = input("Time of travel (hours): ")
        Time = float(Time)

    except:
        print("Invalid input")

    else:
        KmH = Dist / Time
        MpH = KmH * KmhtoMphConst

        print(f"Mile per hours: {MpH}")

# =====================================================================================
"""
viết hàm kiểm tra xem 1 tam giác có là tam giác vuông hay ko
"""

def ex6():
    print("\nPlease input all 3 side of a triangle diameters to check\n")

    try:
        Side1 = input("Side 1 (cm): ")
        Side1 = float(Side1)

        Side2 = input("Side 2 (cm): ")
        Side2 = float(Side2)

        Side3 = input("Side 3 (cm): ")
        Side3 = float(Side3)

    except:
        print("Invalid input")

    else:
        Test1 = Side1 ** 2 + Side2 ** 2
        Test2 = Side2 ** 2 + Side3 ** 2
        Test3 = Side1 ** 2 + Side3 ** 2

        if (
            Test1 == Side3 ** 2 or
            Test2 == Side1 ** 2 or
            Test3 == Side2 ** 2
        ):
            print("\nThe triangle has a square in it\n")
        else:
            print("\nThe triangle does not has a square in it\n")
            