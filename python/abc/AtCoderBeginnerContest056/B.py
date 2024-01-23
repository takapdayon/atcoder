def wab(w,a,b):
    ans = 0
    if w+a >= b and a <= b or a <= b+w and a >= b:
        return ans
    ans = b - (w + a) if a < b else a - (w + b)
    return ans

def main():
    W , a , b = map(int, input().split())
    print(wab(W , a , b))

if __name__ == '__main__':
    main()
