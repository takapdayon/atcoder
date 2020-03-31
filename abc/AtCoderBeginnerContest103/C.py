
def Modulo(n , al):

    return sum(al) - n

def main():
    n = int(input())
    al = list(map(int , input().split()))
    print(Modulo(n , al))

if __name__ == '__main__':
    main()