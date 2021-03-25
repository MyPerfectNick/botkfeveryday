n = int(input())
c = 0
a = list(map(int, input().split()))
fir = a.count(1)
sec = a.count(2)
thir = a.count(3)
c += n - fir - sec - thir
if fir > thir:
    c += thir
    fir -= thir
    c += fir // 4
    fir %= 4
    c += sec // 2
    sec %= 2
    if sec:
        if fir <= 2:
            c += 1
        else:
            c += 2
    else:
        if fir:
            c += 1
elif thir > fir:
    c += fir
    thir -= fir
    c += sec // 2
    sec %= 2
    c += thir
    c += sec
else:
    c += fir
    c += sec // 2
    sec %= 2
    c += sec
print(c)