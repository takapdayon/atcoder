def aberror(a , b):

    return a + b if a + b < 10 else "error"

def main():
    a , b = map(int , input().split())
    print(aberror(a , b))

if __name__ == '__main__':
    main()