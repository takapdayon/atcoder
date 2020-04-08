def ABC(a , b):

    return "No" if (a * b) % 2 == 0 else "Yes"

def main():
    a , b = map(int , input().split())
    print(ABC(a , b))

if __name__ == '__main__':
    main()