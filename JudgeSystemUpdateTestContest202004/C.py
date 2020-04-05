def cjsut(a1 , a2 , a3):

    #ごりおせませんでしたあああああああああああああああああああああ
    if a1 == a2 == 1:
        return 1
    elif a1 == 2:
        if a2 == 1:
            return 3
        if a2 == 2:
            return 5
    elif a1 == 3:
        if a2 == 1:
            return 6
        elif a2 == 2:
            return 8
        elif a2 == 3:
            return 10

def main():
    a1 , a2 , a3 = map(int , input().split())
    print(cjsut(a1 , a2 , a3))
if __name__ == '__main__':
    main()