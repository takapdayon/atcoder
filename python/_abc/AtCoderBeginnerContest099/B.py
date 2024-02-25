def Stone_Mounment(a , b):

    i = b - a

    return i * (i + 1) // 2 - b

def main():
    a , b = map(int , input().split())
    print(Stone_Mounment(a , b))

if __name__ == '__main__':
    main()