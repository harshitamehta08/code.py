n=int(input("enter no. of player you want"))

for i in range(n):
    name=input("enter names:")
    m=int(input("enter no. of matches"))
    total=0

    for ji in range(m):
        score=int(input("enter score:"))
        total+=score
        average=total/n

        print("total",total)
        print("average",average)
