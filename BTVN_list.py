# Bài 00: Viết chương trình sinh list mới bằng cách lấy ngẫu nhiên 5 phần tử từ list gốc.
s = list(input('nhập 1 chuỗi: ').split())
ss = []
for i in range(4):
    ss.append(s[i])
print(ss)
'''///////////////////////////////////////////////////////////////////////'''
# Bài 01: Viết chương trình tính tổng, tích của các phần tử trong một list.
s_01 = list(input('nhap một list: ').split())
tong = 0
tich = 1
for i in range(len(s_01)):
    tong = tong +int(s_01[i])
print('tổng của 1 list day số là {}'.format(tong))
for i in range(len(s_01)):
    tich = tich * int(s_01[i])
print('tích của 1 list day so là {}'.format(tich))
'''///////////////////////////////////////////////////////////////////////'''
# Bài 02: Viết chương trình tìm số lớn nhất, nhỏ nhất trong một list.
s_03 = list(input().split())
# max(s_03)
# min(s_03)
# print(max)
# print(min)
# cho e hỏi lỗi nào fix sao vậy anh
''' <built-in function max>
 <built-in function min>'''
max = 0
min = 10**10
for i in range(len(s_03)):
    if float(s_03[i]) > max :
        max =float(s_03[i])
for i in range(len(s_03)):
    if float(s_03[i]) < min :
        min = float(s_03[i])
print('số lớn nhất trong danh sách đối số là',max)
print('số nhỏ nhất trong danh sách đối số là',min)
'''///////////////////////////////////////////////////////////////////////'''
# Bài 03: Viết chương trình tạo ra list mới bằng cách ghép một chuỗi s vào các phần tử list cũ.
l = list(input('nhập một danh sách : ').split())
s = str(input('nhập một chuỗi : '))
l.append(s)
print(l)
'''///////////////////////////////////////////////////////////////////////'''
# Bài 04: Viết chương trình chia một list thành 2 phần với độ dài phần đầu được nhập vào từ bàn phím.
'''///////////////////////////////////////////////////////////////////////'''
# Bài 05: Viết chương trình in ra phần tử có số lần xuất hiện nhiều nhất trong một list.
#         Nếu có nhiều phần tử có cùng số lần xuất hiện nhiều nhất thì in ra 1 trong số chúng.
l_05 = list(input('nhập 1 list: ').split())
Max = 0
s_max = ''
for i in range(len(l_05)) :
    #print(l_05[i],end=':')
    count = 0
    for j in range(i,len(l_05)):
        if l_05[j] == l_05[i] :
            count = count + 1
    if Max < count :
        Max = count
        s_max = l_05[i]
print(s_max)
'''///////////////////////////////////////////////////////////////////////'''
# Bài 06: Viết chương trình đếm các chuỗi trong một list thỏa mãn:
#         + Độ dài từ 2 trở lên
#         + Ký tự đầu tiên và cuối cùng của chuỗi đó giống nhau
l_06 = list(input('nhập 1 list: ').split())
count = 0
for i in range(len(l_06)):
    if len(l_06[i]) >= 2 and l_06[i][0] == l_06[i][-1] :
       count = count + 1
print('số chuỗi thỏa mãn điều kiện trong list là :', count)
'''///////////////////////////////////////////////////////////////////////'''
# Bài 07: Viết chương trình kiểm tra 2 list có phần tử chung hay không.
l = list(input('nhập vào 2 list : ').split())
temp = ''
s = list(input().split())
for i in range(len(l)):
    for j in range(len(s)):
        if l[i] == s[j]:
            temp ='2 list có chứa phần tử chung '
print(temp)   
'''///////////////////////////////////////////////////////////////////////'''
# Bài 08: Cho list các số nguyên dương A.
#         Xây dựng chương trình đếm số lượng tập gồm 2 phần tử A[i] và A[j] thỏa mãn A[i] > A[j] và i < j.
l = list(input('nhập vào 1 list: ').split())
count = 0
for i in range(len(l)):
    for j in range(i+1,len(l)):
        if l[i] > l[j] and i < j:
            count =count + 1
print ('số cặp phần tử thỏa điều kiện là: ',count)