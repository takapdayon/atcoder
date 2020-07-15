# Atcoder

Atcoderの私用のライブラリ、また私の解答・復習をpushするリポジトリです。
使用言語はPython3です。<br>
(ライブラリ、基本ググって奇麗に整形して持ってきますが、間違い等あればツイッターでお知らせください・・・)


# ライブラリ


# 英文字26loop

```py
for i in range(ord('a'), ord('z') + 1):
    print(chr(i))

```

# 累積和
**特定の範囲の合計値を高速に計算できる**

```py
n = list(int(input()))
nli = [0]*(n + 1)

for i in range(1 , n):
    nli[i + 1] = nli[i] + a[i]
    print(nli[i + 1])
```

**numpy使える場合**
```py
import numpy as np
n = list(int(input()))

nli = np.cumsum(n)
print(nli)
```


# 2次元累積和
**そのうち**
```py

```

# Union Find

**グループわけをしてrootが同じか判定したいとき**

```py
class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())


```

# dict数え上げ
**dictで要素を数え上げたいとき**

```py
from collections import defaultdict

s = str(input())
d = defaultdict(int)

for k in s:
    d[k] += 1

```

# DP

**桁DP**

```py

```

**○○DP**

```py

```

# 指定文字列から文字列変更

**(2 , abcde) → deabc**
```py
def splitmozi(n , s):

    spmozi = ""
    s = list(map(str , s))

    for i in range(len(s)):
        spmozi += s[(-n) + i]

    return spmozi
```

# 約数列挙
**パクってきました**
[ここ](https://qiita.com/LorseKudos/items/9eb560494862c8b4eb56)
```py
def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    # divisors.sort()
    return divisors
```

# 最大公約数
**単体**
```py
def gcd(a , b):
    while b != 0:
        a , b = b , a % b
    return a
```

**複数**
```py
from math import gcd
from functools import reduce

def gcdli(xl):
    #xlはlist
    return reduce(gcd , xl)
```

# 最小公倍数
**単体**
```py
from math import gcd
a = int
b = int
lcm = (a*b // gcd(a, b))
```

**複数**
```py
```

# bit全探索
**python bit全探索で調べてもitertoolsのライブラリ関係の記事ないの辛い**
**重複なし**
```py
import itertools

area = 4
tuplecount = 2
itelist = list(itertools.combinations(range(1, area+1), tuplecount))
print(itelist)
#[(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]
```

**重複あり**
```py
import itertools

area = 4
tuplecount = 2
li = list(itertools.combinations_with_replacement(range(1,area+1), tuplecount))
print(itelist)
#[(1, 1), (1, 2), (1, 3), (1, 4), (2, 2), (2, 3), (2, 4), (3, 3), (3, 4), (4, 4)]
```

**順列**
```py
import itertools

area = 4
tuplecount = 2
irelist = list(itertools.permutations(range(1,area+1), tuplecount))
print(itelist)
#[(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)]
```

# 二分探索
**bisectを使う**
```py
import bisect

searchlist = [3, 5, 2, 6, 1, 2]
searchlist.sort() #[1, 2, 2, 3, 5, 6]
searchint = 2

# left, rightの違いは、同じ値がlistにあった際に、挿入ポイントを左右どちらにするか
print(bisect.bisect_left(searchlist, searchint))
# 1

print(bisect.bisect_right(searchlist, searchint))
# 3
```