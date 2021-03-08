l=[2,3,5,7,1]
l1=[34,45,67]
def sumlist(a):
  sum=0
  for x in a:
    sum+=x
  return sum
print(sumlist(l))
print(sumlist(l1))