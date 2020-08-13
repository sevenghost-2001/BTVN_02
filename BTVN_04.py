a , b , c = float(input()) , float(input()) , float(input())
if a +b > c and a + c > b  and b + c > a :#điều kiện để làm 1 tam giác
    print('a , b , c là 3 cạnh của 1 tam giác . ')
    if a > b and a > c and b ** 2 +c ** 2 == a ** 2 :
        print('đây là một tam giác vuông')
    elif b > c and b > a and a * *2 +c ** 2 == b ** 2 :
        print('đây là một tam giác vuông')
    elif c > b and c > a and a ** 2 +b ** 2 == c ** 2 :
        print('đây là một tam giác vuông')
    else :
        print('đây là tam giác ko vuông',end = ':>')