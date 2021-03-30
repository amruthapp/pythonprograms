s=input("enter a string")
f=s[0]
for x in s:
    if x==f:
        n=(s[1:].replace(x,"$"))
    m=f+n
print(m)
