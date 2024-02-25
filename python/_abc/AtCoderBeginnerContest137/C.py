def green_bin(n, sli):

    ans = 0
    count = {}

    for i in sli:
        i.sort()
        if ''.join(i) in count:
            ans += count[''.join(i)]
            count[''.join(i)] += 1

        else:
            count[''.join(i)] = 1

    return ans

def main():
    n = int(input())
    sli = [list(str(input()))for i in range(n)]
    print(green_bin(n, sli))

if __name__ == '__main__':
    main()