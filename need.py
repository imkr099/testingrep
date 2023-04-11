a = [5, 4, 6, 7, 2]
N = len(a)

for i in range(0, N-1):
    for j in range(0, N-1-i):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]

print(a)