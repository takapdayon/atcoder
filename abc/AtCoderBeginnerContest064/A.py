def four(r , g , b):

    ans = (r*100) + (g*10) + b

    return "YES" if ans % 4 == 0 else "NO"

def main():
    r , g ,b = map(int , input().split())
    print(four(r , g , b))

if __name__ == '__main__':
    main()