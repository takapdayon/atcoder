def christmas(s , a):

    ans = max(a) - min(a)
    return ans

def main():
    s = int(input())
    a = list(map(int , input().split()))
    print(christmas(s , a))

if __name__ == '__main__':
    main()