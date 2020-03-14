
def Product(a , b):

    return "Odd" if (a * b) % 2 == 1 else "Even"

def main():
    a , b = map(int , input().split())
    print(Product(a , b))

if __name__ == '__main__':
    main()
