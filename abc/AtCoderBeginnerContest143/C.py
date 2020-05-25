def slimes(n, sli):

    ans = 0
    sliset = ""

    for i in sli:
        if sliset != i:
            ans += 1
            sliset = i

    return ans

def main():
    n = int(input())
    sli = list(str(input()))
    print(slimes(n, sli))

if __name__ == '__main__':
    main()