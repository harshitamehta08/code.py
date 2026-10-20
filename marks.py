student=int(input("how many students u want "))
subject=int(input("how many subject do you want "))

for i in range(student):
    name=input("\nenter the name:")
    total=0

    for j in range(subject):
        marks=float(input(f"enter marks for subject {j+1}: "))
        total += marks


        average=total/subject

        print("\nname",name)
        print("average marks",average)

        if average >= 33:
            print("result:pass")

        else:
            print("result:fail")    


