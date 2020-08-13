import math
a , b , c = int(input()) , int(input()) , int(input())
if a == 0:
    if b == 0 and c == 0 :
        print('pt có vô số ngiệm')
    else:
        x = - c / b
        print('{} là nghiệm của pt ')
   
else :
    delta = b ** 2 - 4 * a * c
    if delta >0 :
        x1 = (- b - math.sqrt(delta) ) / (2 * a)
        x2 = (- b + math.sqrt(delta) ) / (2 * a)
        print('pt có nghiệm phân biệt là {}, {}' . format(x1,x2))
    elif delta == 0:
        x=- b / ( 2 * a)
        print('pt có ngiệm kép là {}' . format(x))
    else :
        print('pt vô nghiệm')
