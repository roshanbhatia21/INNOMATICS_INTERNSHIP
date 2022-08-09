import numpy
n,m,p=map(int,input().split())
list1=[list(map(int,input().split()))for i in range(n)]
list2=[list(map(int,input().split()))for i in range (m)]
a1=numpy.array(list1)
a2=numpy.array(list2)
print(numpy.concatenate((a1,a2),axis=0))
