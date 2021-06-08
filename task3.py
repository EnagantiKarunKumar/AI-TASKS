a=open("file1.txt","r")
b=open("file2.txt","r")
c=a.read()
d=b.read()
c=c.split(" ")
d=d.split(" ")
for x in range(len(c)):
    c[x]=int(c[x])
for x in range(len(d)):
    d[x]=int(d[x])
print("number of element in file1 is",len(c))
print("number of element in file2 is",len(d))
print("sorted numbers in file1",sorted(c))
print("sorted numbers in file2",sorted(d))
