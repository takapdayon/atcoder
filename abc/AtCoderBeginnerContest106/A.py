def Garden(a , b):

    return a * b - (a + b) + 1

def main():
    a , b = map(int , input().split())
    print(Garden(a , b))

if __name__ == '__main__':
    main()