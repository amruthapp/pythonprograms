l=input("enter the names : ")
w=l.split()
print(w)
count=0
for i in l:
    if i=="a":
        count=count+1
print("the occurrence of a is : ",count)
