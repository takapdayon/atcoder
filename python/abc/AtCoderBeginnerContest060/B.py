def yn(a,b,c):
    ans = "NO"
    for i in range(a*b):
        if a * i % b == c:
            ans = "YES"

    return ans

def main():
    a , b , c = map(int, input().split())
    print(yn(a,b,c))

if __name__ == '__main__':
    main()
