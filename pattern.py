print("   *")
print("  ***")
print(" *****")
print("*******")


# for square pattern
print("\n square")
for i in range(5):
    print(" * " * 5)


# for right traingle
print("\n right traingle")  
for r in range(1,6):
    print(" * " *r)  


# inverted traingle
print("\n inverted traingle")
for p in range(7,0,-1):
    print("* " *p)


# for number traingle
print("\n number traingle")
for e in range(1,6):
    for f in range(1, e + 1):
        print(f, end=" ")
        print()


# same number pattern
print("\n same number")
for k in range (1,6):
    print((str(k)+" ")*k)



# pyramid pattern
print("\n pyramid")
rows=5
for n in range(rows):
    print(" "*(rows-n -1), end="")
    print(" * " * (n+1))
