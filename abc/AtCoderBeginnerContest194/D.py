def math(x):
    ans = 0
    for i in range(1, 10):
        kae = 1 if str(x).count(str(i)) == 9 else 10**str(x).count(str(i))
        ans += i * kae
    return ans

def d194():

    

k = int(input())
s = str(input())
t = str(input())
print(d194())
