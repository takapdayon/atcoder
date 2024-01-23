v, t, s, d = map(int, input().split())
print('No' if (t*v) <= d <= (s*v) else 'Yes')