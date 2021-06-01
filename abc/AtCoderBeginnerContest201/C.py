def c201(s):
    # 何通りあるか、多くても1000通り
    # 1000通りの中から、使えない文字を除外していく
    maru = 0
    hatena = 0
    if s.count("o") > 4:
        return 0
    for i in s:
        if i == "o":
            maru += 1
        elif i == "?":
            hatena += 1

    zenbu = (maru+hatena)

    if maru == 4:
        return 4 * 3 * 2

    if maru == 3:
        return zenbu - (3 * (maru+hatena - 1) ** 4 + (hatena) ** 4)

    if maru == 2:
        return zenbu - (( * (maru+hatena - 1) ** 4) + (hatena) ** 4)

    if maru == 1:
        return zenbu ** 4 - (zenbu - 1) ** 4

    if maru == 0:
        return hatena ** 4

s = list(str(input()))
print(c201(s))
