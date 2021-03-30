dic={'zayan':11,'aami':20,'baby':20}
l=list(dic.items())
l.sort()
print("ascending order is : ",l)
l.sort(reverse=True)
print("descending order is : ",l)
dict=dict(l)
print("dictionary is: ",dict)
