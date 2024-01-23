import math

def Minimization(n , k , al):

    ans = math.ceil((n - 1) / (k - 1))

    return ans

def main():
    n , k = map(int , input().split())
    al = list(map(int , input().split()))
    print(Minimization(n , k , al))

if __name__ == '__main__':
    main()