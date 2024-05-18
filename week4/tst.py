import os 
def ex9():
    filename = input("\nwhat is the file name: ")

    # find the file path in the user desktop
    for root, dirs, files in os.walk("C:\\Users\\PC\\Desktop\\"):
        for name in files:
            if name == filename:
                print(os.path.abspath(os.path.join(root, name)))

    print()
    
ex9()