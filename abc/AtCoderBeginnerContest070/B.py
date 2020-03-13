def twoswiches(a , b , c , d):

    ans = min(b , d) - max(a , c)
    return ans if ans > 0 else 0

def main():
    a , b , c , d = map(int , input().split())
    print(twoswiches(a , b , c , d))

if __name__ == '__main__':
    main()