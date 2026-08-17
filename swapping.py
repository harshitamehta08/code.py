# without third variable
a=10
b=5
a,b = b,a
print("swapping:")
print(a)
print(b)




# with third variable
x=23
y=67
z=x
x=y
y=z
print("swapping:")
print(x)
print(y)



# with the help of multiplication/divide
q=3
r=9

q=q*r
r=q//r
q=q//r
print("swap:")
print(q)
print(r)


#  swap first and last emlement of list
print("last to first:")
numb = [10,20,30,40,50]
numb[0], numb[-1] = numb[-1],numb[0]

print(numb)



# swap using a function
print("function:")
def swap(g,j):
    return j,g
g=20
j=30
g,j=swap(g,j)
print(g,j)




print("function using 3rd variable")
def swap(p,v):
    temp= p
    p=v
    v=temp
    return p,v

p,v = swap(22, 33)
print(p,v)



# 3 variable swap
print("3 var:")
s=5
d=6
f=7
s,d,f=f,s,d
print(s,d,f)


# swaping by additon
print("additon")
w=30
m=20
w=w+m
m=w-m
w=w-m
print(w,m)



# user and swap them
t=int(input("enter number:"))
u=int(input("enter number:"))
t,u = swap(t,u)
print(t,u)



# user with 3rd variable
l=int(input("enter number:"))
n=int(input("enter number:"))
swa=l
l=n
n=swa
print(l,n)
