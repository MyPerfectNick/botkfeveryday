for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    i = 0
    for k in range(1, n + 1):
        if not a[k - 1] % 2:
            print(1)
            print(k)
            break
        elif i:
            print(2)
            print(i, k)
            break
        else:
            i = k
    else:
        print(-1)
