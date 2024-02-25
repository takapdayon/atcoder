def saiki(n, s, ks, loops):

    count = ks + s
    ans = 0

    if int(count) > int(n):
        return 0
    elif "3" in count and "5" in count and "7" in count:
        ans += 1

    for i in loops:
        ans += saiki(n, i, count, loops)

    return ans

def b755(n):


    loops = ["3", "5", "7"]
    ans = 0

    for i in loops:
        ans += saiki(n, i, "", loops)

    return ans

def main():
    n = str(input())
    print(b755(n))

if __name__ == '__main__':
    main()
