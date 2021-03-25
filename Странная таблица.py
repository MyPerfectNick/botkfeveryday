for _ in range(int(input())):
    n, m, x = map(int, input().split())
    j = (x - 1) % n
    print(m * j + (x - 1) // n + 1)
