import time as t
a=int(input())
b=int(input())
c=input()
q=800
r=0
p=100/q
for buf in range(q):
    print('Обработка файлов завершена на %3d%%\r' % r, end = '', flush = True)
    t.sleep(0.001)
    r+=p
c=list(c)
e=0

if a>10:
    while e<len(c):
        d=c[e]
        if d=='A':
            c[e]='10 '
        if d=='B':
            c[e]='11'
        if d=='C':
            c[e]='12'
        if d=='D':
            c[e]='13'
        if d=='E':
            c[e]='14'
        if d=='F':
            c[e]='15'
        e+=1

c=list(map(int, c))
y=len(c)
e=0
i=0
z=0
while i<y:
    o=-(i+1)
    q=c[o]
    x=q*(a**i)
    z=z+x
    i+=1
qmqm=[]
while z>=b:
    qw=z%b
    z=z//b
    qmqm.insert(0, qw)
qmqm.insert(0, z)
qmqm=list(map(str, qmqm))
if b>10:
    while e<len(c):
        d=c[e]
        if d=='10':
            c[e]='A'
        if d=='11':
            c[e]='B'
        if d=='12':
            c[e]='C'
        if d=='13':
            c[e]='D'
        if d=='14':
            c[e]='E'
        if d=='15':
            c[e]='F'
        e+=1
a=0
b=''
z=[]
z=qmqm
x=len(qmqm)
while a<x:
    p=qmqm[a]
    b=b+p
    a+=1
print(b)