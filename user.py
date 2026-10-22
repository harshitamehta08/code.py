a=int(input("enter the no. you want: "))
b=[]
total=0
for i in range(a):
    c=int(input("enter the of teams u want:"))
    d=int(input("scores:"))
    
    
    b.append(d)
    
    total+=d
    print("team score:",b)
    print("total score:",total)
    if a>0:
        average=total/a
        print("average")
    