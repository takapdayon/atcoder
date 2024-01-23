import fractions

def lcm(x, y):
    return (x * y) // fractions.gcd(x, y)

def saiki(n , t , maxi):

    saikimaxi = 0
    for i in range(n):
        if maxi % t[i] != 0:
            saikimaxi = max(saikimaxi , t[i])

    if saikimaxi != 0:
        return saiki(n , t , lcm(maxi , saikimaxi))
    else:
        return maxi

def multiclocks(n , t):

    maxi = max(t)
    return saiki(n , t , maxi)

def main():
    n = int(input())
    t = [int(input()) for i in range(n)]
    print(multiclocks(n , t))

if __name__ == '__main__':
    main()