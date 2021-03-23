for _ in range(int(input())):
    s = input()
    length = len(s)
    if length > 10:
        print(s[0], length - 2, s[-1], sep="")
    else:
        print(s)

