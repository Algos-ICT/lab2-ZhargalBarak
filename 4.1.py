f = open('input.txt')
A = list(map(int, f.readline().split()))
V = int(f.readline())
f.close()
b = []
for i in range(len(A)):
    if A[i] == V:
        b.append(i+1)
f = open('output.txt', 'w')
if len(b) == 0:
    f.write('-1')
else:
    for i in range(len(b) - 1):
        f.write(str(b[i]) + ', ')
    f.write(str(b[len(b) - 1]))
f.close()