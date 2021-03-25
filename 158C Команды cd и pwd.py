s = []
for _ in range(int(input())):
    t = input()
    if t == "pwd":
        if s:
            print("/" + "/".join(s) + "/")
        else:
            print("/")
    else:
        path = t[3:]
        if path.startswith("/"):
            s = []
            path = path.split("/")[1:]
        else:
            path = path.split("/")
        for s1 in path:
            if s1 == "..":
                s.pop()
            else:
                s.append(s1)
