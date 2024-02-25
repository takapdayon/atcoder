import sys
from math import sqrt

# input = sys.stdin.readline
def i_input(): return int(input())
def i_map(): return map(int, input().split())
def i_list(): return list(i_map())
def i_row(N): return [i_input() for _ in range(N)]
def i_row_list(N): return [i_list() for _ in range(N)]
def s_input(): return input()
def s_map(): return input().split()
def s_list(): return list(s_map())
def s_row(N): return [s_input() for _ in range(N)]
def s_row_str(N): return [s_list() for _ in range(N)]
def s_row_list(N): return [s_list() for _ in range(N)]

num_list = []
str_list = []

def distance(x1, y1, x2, y2):
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def main():
    n = i_input()
    xyrows = i_row_list(n)
    xyrows = set(xyrows)
    result = 0

    for fi in range(n - 1):
        for se in range(fi + 1, n):
            # 2点与えられて他2点を同じ方向で探索
            x_l = abs(xyrows[fi][0] - xyrows[se][0])
            y_l = abs(xyrows[fi][1] - xyrows[se][1])
            if (xyrows[fi][0] + y_l, xyrows[fi][1] + x_l) in xyrows and (xyrows[se][0] + y_l, xyrows[se][1] + x_l) in xyrows:
                result = max(result, distance(xyrows[fi][0], xyrows[fi][1]) ** 2)

    print(int(result))

if __name__ == '__main__':
    main()

# テスト: oj t -c 'poetry run python main.py'
# 提出: acc s main.py -- --guess-python-interpreter pypy
# 再帰あるとき:  acc s main.py -- --guess-python-interpreter cpython --language 5055
