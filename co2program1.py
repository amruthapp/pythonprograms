a=int(input("enter a number"))
fact=1
if a<0:
  print("sorry, factorial of negative numbers doesn't exist")
elif a==0:
  print("the factorial of 0 is 1")
else:
  for i in range(1,a+1):
     fact=fact*i
  print("factorial of ", a,"is ", fact)
