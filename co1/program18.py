def merge(dict1,dict2):
    return(dict1.update(dict2))
dict1={'a':2,'b':5}
dict2={'c':9,'d':10}
print(merge(dict1,dict2))
print(dict1)
