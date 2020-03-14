def Good_Sequence(n , al):

    count = {}
    ans = 0

    for i in al:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1

    for i in count.keys():
        key = int(i)
        value = int(count[i])
        if key != value:
            ans += value if value < key else abs(key - value)

    return ans

def main():
    n = int(input())
    al = list(map(int , input().split()))
    print(Good_Sequence(n , al))

if __name__ == '__main__':
    main()
