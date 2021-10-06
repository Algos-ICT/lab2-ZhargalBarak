f = open('input.txt')
n = int(f.readline())
c = list(map(int, f.readline().split()))
f.close()
for j in range(n):
    cur = c[j]
    i = j - 1
    while i >= 0 and cur < c[i]:
        c[i+1] = c[i]
        i -= 1
    c[i+1] = cur
f = open('output.txt', 'w')
for i in range(n):
    f.write(str(c[i]) + ' ')
f.close()