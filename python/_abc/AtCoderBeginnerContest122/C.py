def get_ac(n, q, s, lrli):

    ans = []
    nli = [0]*(n+1)

    for i in range(1, n):
        if s[i] == "C" and s[i-1] == "A":
            nli[i+1] = nli[i] + 1
        else:
            nli[i+1] = nli[i]

    for i in lrli:
        ans.append(nli[i[1]]-nli[i[0]])

    return ans

def main():
    n, q = map(int, input().split())
    s = list(str(input()))
    lrli = [list(map(int, input().split()))for i in range(q)]
    ans = get_ac(n, q, s, lrli)
    for i in ans:
        print(i)

if __name__ == '__main__':
    main()