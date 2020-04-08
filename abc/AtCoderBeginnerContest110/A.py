def Maximize(abc):

    abc.sort(reverse=True)

    return abc[0] * 10 + abc[1] + abc[2]

def main():
    abc = list(map(int , input().split()))
    print(Maximize(abc))

if __name__ == '__main__':
    main()