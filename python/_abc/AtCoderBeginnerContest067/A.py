def yagi(a , b):
    ans = ""

    if a % 3 == 0 or b % 3 == 0 or (a + b) % 3 == 0:
        ans = "Possible"
    else:
        ans = "Impossible"

    return ans

def main():
    a , b= map(int , input().split())
    print(yagi(a , b))

if __name__ == '__main__':
    main()