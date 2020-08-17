
#Viết chương trình để xóa các ký tự có số lẻ là số lẻ trong một chuỗi
import re
s =  str(input())
for i in range(1, len(s)+1) :
    if i %2 !=0 :
        if format(ord(s[i]) % 2 != 0) :
            s =re.sub(s[i], "", s)
print(s)

#print(format(ord(c)))
'''anh cho em hỏi tại sao em viết 3 ký tự thì nó chạy dc
input:asd
output:ad
còn nếu em viết hơn 3 ký tự thì nó ra lỗi
index out of range