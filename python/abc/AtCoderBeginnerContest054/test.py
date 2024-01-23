A = int(input())

def ab(A):
    print(A)
    if A == 0:
        return "end"
    else:
        A -= 1
        ab(A)

if __name__ == '__main__':
    ans = ab(A)
    print(ans)