
def Coins(a , b , c , x):

    count = 0

    for i in range(a+1):
        for w in range(b+1):
            for q in range(c+1):
                if 500*i + 100*w + 50*q == x:
                    count += 1

    return count

def main():
    a = int(input())
    b = int(input())
    c = int(input())
    x = int(input())
    print(Coins(a , b , c , x))

if __name__ == '__main__':
    main()
