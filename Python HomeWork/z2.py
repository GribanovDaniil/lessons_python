ac=int(input(''))
b = []
while a!=0:
    if a > 2 and a<=5:
        b.append(a)
    a = int(input(''))
print(sum((b.count(3),b.count(4),b.count(5)))/len(b)+100)