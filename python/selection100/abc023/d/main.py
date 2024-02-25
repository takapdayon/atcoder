def i_input(): return int(input())
def i_map(): return map(int, input().split())
def i_list(): return list(i_map())
def i_row_list(N): return [i_list() for _ in range(N)]

def is_ok(n, hsrows, mid):
    t = [0] * n
    res = True
    for i in range(n):
        t[i] = ((mid - hsrows[i][0]) / hsrows[i][1])
    sorted(t)
    for i in range(n):
        if t[i] < i:
            res = False
    return res

def main():
    n = i_input()
    hsrows = i_row_list(n)
    le, ri = 0, 10 ** 18
    while abs(le - ri) > 1:
        mid = (le + ri) // 2
        if is_ok(n, hsrows, mid):
            ri = mid
        else:
            le = mid
    print(ri)

if __name__ == '__main__':
    main()

# テスト: oj t -c 'poetry run python main.py'
# 提出: acc s main.py -- --guess-python-interpreter pypy
# 再帰あるとき:  acc s main.py -- --guess-python-interpreter cpython --language 5055
