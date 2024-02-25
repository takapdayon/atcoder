def d198(s1, s2, s3):
    # どう頑張っても足りない場合
    # or
    # どう頑張ってもoverする場合にerror
    count = [chr(i) for i in range(ord('a'), ord('z') + 1) if chr(i) in f"{s1}{s2}{s3}"]
    if len(count) > 10:
        return "UNSOLVABLE"
    if len(s1) > len(s3) or len(s2) > len(s3):
        return "UNSOLVABLE"

    

    return

s1 = str(input())
s2 = str(input())
s3 = str(input())
print(d198(s1, s2, s3))
