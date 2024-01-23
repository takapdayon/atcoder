def sharpimage(h , w , a):

    reans = []
    aa = ""

    for i in range(w + 2):
        aa += "#"

 #   for i in range(h):
    for i in a:
        reans.append("#" + i + "#")

    reans.insert(0 , aa)
    reans.append(aa)

    return reans

def main():
    h , w = map(int, input().split())
    a=[str(input()) for i in range(h)]

    ans = sharpimage(h , w , a)
    for i in range(len(ans)):
        print(ans[i])

if __name__ == '__main__':
    main()