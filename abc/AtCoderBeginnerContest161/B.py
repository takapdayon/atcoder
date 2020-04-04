def b161(n , m , al):

    ans = "Yes"
    al.sort(reverse=True)
    gou = sum(al)

    for i in range(m):
        if al[i] < gou / (4 * m):
            ans = "No"

    return ans

def main():
    n , m = map(int , input().split())
    al = list(map(int , input().split()))
    print(b161(n , m , al))

if __name__ == '__main__':
    main()