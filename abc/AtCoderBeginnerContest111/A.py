def Atcoder999(n):

    return n.replace("9" , "5").replace("1" , "9").replace("5" , "1")

def main():
    n = str(input())
    print(Atcoder999(n))

if __name__ == '__main__':
    main()