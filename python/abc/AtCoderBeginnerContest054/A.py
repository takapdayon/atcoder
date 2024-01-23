A , B = map(int , input().split())

def aorb(A , B):
    if A == B:
        return "Draw"
    elif A == 1 or A > B and B != 1:
        return "Alice"
    else:
        return "Bob"

if __name__ == '__main__':
    ans = aorb(A , B)
    print(ans)