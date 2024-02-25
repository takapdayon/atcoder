def happy(a , b):

    return "Yay!" if a <= 8 and b <= 8 else ":("

def main():
    a , b = map(int , input().split())
    print(happy(a , b))

if __name__ == '__main__':
    main()