#4.1 task
a = 5.08
b = 5.33
c = 5.55
d = b - a
e = c - b
if d < e:
    print("the change between 2014 and 2025 is larger, and the population growth accelerates")
else:
    if d == e:
        print("the change between 2014 and 2025 is same as the change between 2004 and 2015, and the population growth neither accelerates nor decelerates")
    else:
        print("the change between 2004 and 2015 is larger, and the population growth decelerates")
#
#4.2 task
print("\n")
X = True
Y = False
W = X or Y
print("X\tY\tW")
bools = [True, False]
for X in bools:
    for Y in bools:
        W = X or Y
        print( X,"\t",Y,"\t",W)

# Truth table for X,Y,Z:
#X       Y       W
#True     True    True
#True     False   True
#False    True    True
#False    False   False