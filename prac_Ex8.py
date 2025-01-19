N = int(input())
ls = []
for _ in range(N):
    s = input().split()
    cmd = s[0]
    s_ = s[1:]
    args = s_
    if cmd != "print":
        cmd += "(" + ",".join(args) + ")"
        eval("l."+cmd)
    else:
        print(ls)
