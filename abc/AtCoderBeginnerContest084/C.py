def Multiple_Gift(x , y):

    ans = 1

    while x < y:
        if x * 2 <= y:
            ans += 1
        x = x * 2

    return ans

def main():
    x , y = map(int , input().split())
    print(Multiple_Gift(x , y))

if __name__ == '__main__':
    main()
