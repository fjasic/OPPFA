import sys
print("unesi N")
n=int(sys.argv[1])
x=0
while(n>0):
    x=x+n**2
    n=n-1
print("n brojeva na kvadrat",x)