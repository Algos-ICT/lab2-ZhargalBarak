f = open('input.txt')
n = int(f.readline())
s = f.readline()
f.close()
if n == 1:
    pal = s
else:
    s = sorted(s)
    flag = False
    pal = ''
    mid = ''
    for i in range(n-1):
        if s[i] == s[i+1]:
            s[i+1] = ""
            pal += s[i]
        else:
            if flag is False:
                if s[i] != "":
                    mid = s[i]
                    flag = True
                elif i == n-2:
                    mid = s[i+1]
                    flag = True
    pal = pal + mid + pal[::-1]
f = open('output.txt', 'w')
f.write(pal)
f.close()