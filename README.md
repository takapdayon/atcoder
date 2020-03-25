# Atcoder

Atcoder の私用のライブラリ、また私の解答・復習を push するリポジトリです。
使用言語は Python3 です。
(ライブラリ、基本ググって奇麗に整形して持ってきますが、間違い等あればツイッターでお知らせください・・・)

# 自分の解答状態

- 非常に便利なサイトです。自分の Rank がわかりますね。目指せ challenger [https://kenkoooo.com/atcoder/](https://kenkoooo.com/atcoder/)

# ライブラリ

# union Find

**コピ pe**

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

    def union(self, x, y):
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
