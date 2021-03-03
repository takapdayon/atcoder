def math(x):
    ans = 0
    for i in range(1, 10):
        kae = 1 if str(x).count(str(i)) == 9 else 10**str(x).count(str(i))
        ans += i * kae
    return ans

def d193(k, s, t):
    """
    組み合わせの数は: 9*9の81パターン
    確率の総数は: (9*k - 8) * (9*k - 8 - 1)

    組み合わせの81パターンを列挙中に、勝った場合,kに比例した数をansに加えて
    最後に総数((9*k - 8) * (9*k - 8 - 1))で割る
    """

    ans = 0

    for i in range(1, 10):
        for w in range(1, 10):
            if math(s.replace('#', str(i))) > math(t.replace('#', str(w))):
                # ここでansにkに比例した数をたす
                # その際に既に使われている数は引いて計算する
                if i == w:
                    ans += (k - f'{s}{t}'.count(str(i))) * ((k - f'{s}{t}'.count(str(i))) - 1)
                    continue
                ans += (k - f'{s}{t}'.count(str(i))) * (k - f'{s}{t}'.count(str(w)))

    return ans / ((9*k - 8) * (9*k - 8 - 1))

k = int(input())
s = str(input())
t = str(input())
print(d193(k, s, t))
