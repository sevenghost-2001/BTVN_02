n =  int(input())
s = 0
if(n >= 1000) :
    n=int(input())
sbd = n
for i in range( 0 , 3 ) :
    
    temp = n % 10
    s = s+ temp
    n = int(n / 10)
print( '{} là tổng của các chữ số trong {} ' . format(s , sbd ) )  
