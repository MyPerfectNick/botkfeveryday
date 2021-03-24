n, k = map(int, input().split())
b = [int(i) for i in input().split()]
y = b[k - 1]  # номер начинается с 1
print(len([x for x in b if x >= y and x > 0]))
