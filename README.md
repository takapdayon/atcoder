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

**コピpe**

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