a=int(input("enter the first number"))
b=int(input("enter the second number"))
c=int(input("enter the third number"))
if a>b:
  if a>c:
    print("a is bigger")
  else:
    print("c is bigger")
elif b>c:
  print("b is bigger")
else:
  print("c is bigger")