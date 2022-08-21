n=int(input())
a=list(map(int,input().split()))
m=a[-1]
a.remove(a[-1])
lis=[]
for i in range(n-m):
    lis.append(sum(a[i:i+m]))
print(sum(a)-max(lis))
