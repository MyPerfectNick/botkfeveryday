gc = 0
for _ in range(int(input())):
    s = input()
    c = s.count("1")
    if c >= 2:
        gc += 1
print(gc)
