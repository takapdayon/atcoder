def Otoshidama(n , y):

    for i in range(n + 1):
        for w in range(n - i + 1):
            if (10000*i) + (5000*w) + (1000*(n - (i + w))) == y:
                return str(i) + " " + str(w) + " " + str(n - (i + w))

    return "-1 -1 -1"

def main():
    n , y = map(int , input().split())
    print(Otoshidama(n , y))

if __name__ == '__main__':
    main()
