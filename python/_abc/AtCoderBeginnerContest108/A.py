def Pair(k):

    return int((k / 2)**2) if k % 2 == 0 else int((k // 2) * (k // 2 + 1))

def main():
    k = int(input())
    print(Pair(k))

if __name__ == '__main__':
    main()