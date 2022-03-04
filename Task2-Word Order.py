from collections import OrderedDict
a=OrderedDict()
n=int(input())
for i in range(n):
    o=input()
    if o in a.keys():
        a[o]+=1
    else:
        a[o]=1
print(len(a.keys()))
print(' '.join([str(a[k]) for k in a.keys()]))