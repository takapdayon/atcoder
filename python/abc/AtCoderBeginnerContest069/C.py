def adjacent4(n , a):

    ans = "No"
    zero = 0
    iti = 0
    ni = 0

    for i in range(n):
        if a[i] % 2 == 1:
            zero += 1
        elif (a[i] / 2) % 2 == 0:
            ni += 1
        else:
            iti += 1

    if iti > 0 and zero <= ni:
        ans = "Yes"
    elif iti == 0 and zero <= ni + 1:
        ans = "Yes"
    return ans

def main():
    n = int(input())
    a = list(map(int,input().split()))
    print(adjacent4(n , a))

if __name__ == '__main__':
    main()