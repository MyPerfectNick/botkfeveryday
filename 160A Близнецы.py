n = int(input())
m = sorted(list(map(int, input().split())))
fir = c = 0
sec = sum(m)
while fir <= sec:
    fir += m[-1]
    sec -= m[-1]
    m.pop()
    c += 1
print(c)