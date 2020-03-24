def Maximum_Sum(a , b , c , k):

    return a + b + c - max(a , b , c) + max(a , b , c) * (2**k)

def main():
    a, b, c = map(int, input().split())
    k = int(input())
    print(Maximum_Sum(a , b , c , k))

if __name__ == '__main__':
    main()