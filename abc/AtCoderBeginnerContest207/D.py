import bisect

def d205(n, q, alist, kq):
    # その数までの出現回数を足して出力すればいいだけ
    ans = []

    for k in kq:
        before = 0
        count = k
        while True:
            result = bisect.bisect_right(alist, count)
            if result - before == 0:
                ans.append(result + k)
                break

            count += result
            before = result
    return ans

n, q = map(int, input().split())
alist = list(map(int, input().split()))
kq = [int(input()) for _ in range(q)]
ans = d205(n, q, alist, kq)
for a in ans:
    print(a)