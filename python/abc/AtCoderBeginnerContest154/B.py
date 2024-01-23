def has_duplicates(seq):
    return len(seq) != len(set(seq))

def onlya(n , a):

    ans = "YES"

    if has_duplicates(a):
        return "NO"

    return ans

def main():
    n = int(input())
    a = list(map(int,input().split()))
    print(onlya(n , a))

if __name__ == '__main__':
    main()