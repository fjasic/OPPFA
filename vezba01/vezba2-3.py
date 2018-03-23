import sys
x=sys.argv[1]
y=sys.argv[2]
duzina=len(y)
z=x[0:3] + x[0:3] + y[duzina-3:duzina] + y[duzina-3:duzina]
print("dobijeni string je",z)