def please(n , a):

    for i in range(n):
        if a[i] % 2 == 0:
            if a[i] % 3 != 0 and a[i] % 5 != 0:
                return "DENIED"
    
    return "APPROVED"

def main():
    n = int(input())
    a = list(map(int,input().split()))
    print(please(n , a))

if __name__ == '__main__':
    main()