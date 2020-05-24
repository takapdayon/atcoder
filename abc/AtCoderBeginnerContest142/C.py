def go_to_school(n, ali):

    ans = [0]*n

    for i in range(n):
        ans[ali[i]-1] = i+1

    return ans

def main():
    n = int(input())
    ali = list(map(int, input().split()))
    print(*go_to_school(n, ali))

if __name__ == '__main__':
    main()