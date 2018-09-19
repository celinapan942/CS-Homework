a = [0,0,0,0,1,1,1,1]
b = [0,0,1,1,0,0,1,1]
c = [0,1,0,1,0,1,0,1]

for n in range (0,7):
    print int(((a[n] and b[n]) or not(a[n] and c[n])))
