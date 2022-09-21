first = int(input('К оплате:'))
second = int(input('К оплате:'))
third = int(input('К оплате:'))
if first > second and second > third:
    print ('Акция!',sum([first, second, third])/3)
elif first < second and second < third:
    print ('Акция!', sum([first, second, third])/2)
else:
    print('К оплате:')