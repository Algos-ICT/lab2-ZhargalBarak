f = open('input.txt')
n = int(f.readline())
A, B = map(str, f.readline().split())
f.close()
summary = []
for _ in range(n+1):
    summary.append(0)
for i in range(n-1, -1, -1):
    summary[i+1] += int(A[i]) + int(B[i])
    if summary[i+1] >= 2:
        summary[i] += 1
        if summary[i+1] == 3:
            summary[i+1] = 1
        else:
            summary[i+1] = 0
f = open('output.txt', 'w')
for i in range(n+1):
    f.write(str(summary[i]))
f.close()