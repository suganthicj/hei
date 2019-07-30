x11=input()
y11=0
z11=0
for o in range(len(x11)):
    if x11[o]=="(":
        y11=y11+1
    if x11[o]==")":
        z11=z11+1
if y11==z11:
    print("yes")
else:
    print("no")
