from itertools import combinations
 
def i_input(): return int(input())
def i_map(): return map(int, input().split())
def i_list(): return list(i_map())
def i_row(N): return [i_input() for _ in range(N)]
def i_row_list(N): return [i_list() for _ in range(N)]
def s_input(): return input()
def s_map(): return input().split()
def s_list(): return list(s_map())
 
n, p, q = i_map()
alist = i_list()
combs = combinations(alist, 5)
result = 0

for a1, a2, a3, a4, a5 in combs:
    if a1 % p * a2 % p * a3 % p * a4 % p * a5 % p == q:
        result += 1
print(result)