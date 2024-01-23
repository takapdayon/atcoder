def kth_common_divisor(a, b, k):

    count = []
    for i in range(1, max(a, b)+1):
        if a%i == 0 and b%i == 0:
            count.append(i)

    count.sort(reverse=True)
    return count[k-1]

def main():
    a, b, k = map(int, input().split())
    print(kth_common_divisor(a, b, k))

if __name__ == '__main__':
    main()
