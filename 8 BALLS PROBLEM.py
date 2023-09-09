#8 BALLS PROBLEM
a=[10,10,10,9,10,10,10,10]
b1=[]
b2=[]
b3=[]
s1=0
s2=0 
s3=0 
for i in range(0,3):
    b1.append(a[i])
for i in range(3,6):
    b2.append(a[i])
for i in range(6,8):
    b3.append(a[i])
print(b1,b2,b3)
for i in b1:
    s1+=i 
for j in b2:
    s2+=j
for k in b3:
    s3+=k
print(s1,s2,s3)
if s1==s2:
    if b3[0]>b3[1]:
        print(b3[1],"is defective.")
    else:
        print(b3[0],"is defective.")
elif s1>s2:
    if b2[0]==b2[1]:
        print(b2[2],"defective")
    if (b2[0]>b2[1]):
        print(b2[1])
    if (b2[1]>b2[0]):
        print(b2[0])
elif s1<s2:
    if b1[0]==b1[1]:
        print(b1[2],"defective")
    if (b1[0]>b1[1]):
        print(b1[1])
    if (b1[1]>b1[0]):
        print(b1[0])
else:
    print("no defective item found")
        
        