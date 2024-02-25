
def shiftonly(n , al):

    ans = 0
    flag = True

    while flag:
        for i in range(n):
            if al[i] % 2 == 1:
                flag = False
                break
            else:
                al[i] = al[i] / 2
        if flag:
            ans += 1


    return ans

def main():
    n = int(input())
    al = list(map(int , input().split()))
    print(shiftonly(n , al))

if __name__ == '__main__':
    main()
