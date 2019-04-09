

import random as r
def num():
    x=int(r.random()*100)
    for i in range(50):
        x=int(r.random()*100)  
    return x
a=[]
for i in range(50):
    a.append(num())
print(' ')
print(a)
a.sort()

# print(a)

f=open(r'C:\Users\HUAWEI\Desktop\python\liu.txt','w')
for i in range(50):
    f.write(str(a[i])+' ')
f.write("\n")
f.close()
f=open(r'C:\Users\HUAWEI\Desktop\python\liu.txt','r')
print(f.read())
a.reverse()
f=open(r'C:\Users\HUAWEI\Desktop\python\liu.txt','a')
for i in range(50):
    f.write(str(a[i])+' ')
f.close()
f=open(r'C:\Users\HUAWEI\Desktop\python\liu.txt','r')
print(f.read())