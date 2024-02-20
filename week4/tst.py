def main():
    n = int(input("what's n? "))
    for x in sheep(n):
        print(x)


def sheep(n):
    for i in range(n):
        yield "🍊" * i

if __name__ == "__main__":
    main()
