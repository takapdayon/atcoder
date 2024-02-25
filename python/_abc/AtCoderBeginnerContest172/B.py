def b172(slist, tlist):

    ans = 0

    for s, t in zip(slist, tlist):
        if s != t:
            ans += 1

    return ans

def main():
    slist = list(str(input()))
    tlist = list(str(input()))
    print(b172(slist, tlist))

if __name__ == '__main__':
    main()