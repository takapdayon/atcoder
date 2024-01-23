def a165(k, a, b):

    ans = "NG"
    count = k
    while count <= 1100:
        if a <= count <= b:
            ans = "OK"
            break
        else:
            count += k

    return ans
def main():
    k = int(input())
    a, b = map(int, input().split())
    print(a165(k, a, b))

if __name__ == '__main__':
    main()