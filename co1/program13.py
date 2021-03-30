n=int(input("enter the number of colors : "))
list=[]
for i in range(n):
    a=input("enter the color : ")
    list.append(a)
print(list)
print("the first color is : ",list[0])
print("the last color is : ",list[-1])
