n = int(input())
integer_tpl = list(map(int, input().split()))
t = tuple(integer_tpl)
print(hash(t))