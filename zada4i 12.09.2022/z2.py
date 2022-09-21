a = int(input('К оплате:'))
b = int(input('Текущий час:'))
if b >= 10 and b <= 12:
    a = a/2
    print('Счастливые часы, к оплате:', a)
if b >= 20 and b <= 22:
    a = a/4
    print ('Счастливые часы, к оплате:', a)
if b > 8 and b < 10 or b > 12 and b < 20:
    print ('К оплате:', a)