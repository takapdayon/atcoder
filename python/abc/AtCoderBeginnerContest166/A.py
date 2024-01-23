def a166(s):

    ans = {"ABC":"ARC", "ARC":"ABC"}

    return ans[s]
def main():
    s = str(input())
    print(a166(s))

if __name__ == '__main__':
    main()