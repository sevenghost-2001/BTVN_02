import re
s = str(input())
temp = s
for i  in range(len(s)) :
    if i > 1 :    
        if s[i] == s[0] :
            s =re.sub(s[i], '$', s)   #lệnh này có tác dụng gán str thành 1 str mới   
print(s)
 '''tại sao khi bỏ if i > 1 thì nó lại ra 
input: haha      
output:$a$a$
còn có thì ra
output:$a$a
tại sao lệnh replace ko có tác dụng thay thế khi thoát ra khỏi hàm for
'''