x , n = int(input()) , int(input())
s1 = s2 = 1
s3 = 1.0
z = 1#biến giai thừa
#tính s1
for i in range(1 , n+1 ) :
    s1 = s1 + x ** i
print('giá trị của s1 là : ', s1 )
#tính s2
for i in range(1, n+1 ) :
    s2 = s2 + (- 1) ** i * x ** i 
print('giá trị của s2 là : ', s2 )
#tính s3
for i in range(1 , n + 1) :
    z= z * i
    s3 = s3 + float (x/z)

print('giá trị của s3 là : ', s3 )

