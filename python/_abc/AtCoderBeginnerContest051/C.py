sx , sy , tx , ty = map(int , input().split())

ans = ""
ans2 = ""

for u in range(ty - sy):
    ans += "U"
for r in range(tx - sx):
    ans += "R"

ans2 = "LU" + ans + "RD"


#print(ans + ans.replace("U","D").replace("R":"L") + ans2 + ans2.replace("U","D").replace("R":"L"))
print(ans + ans.translate(str.maketrans('UR', 'DL')) + ans2 + ans2.translate(str.maketrans('UR', 'DL')))