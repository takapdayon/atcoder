def b198(n):

    if n == ''.join(reversed(n)):
        return "Yes"

    for i in range(len(n)):
        s = f"{'0'*i}{n}"
        if s == ''.join(reversed(s)):
            return "Yes"

    return "No"

n = str(input())
print(b198(n))
