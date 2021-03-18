a=int(input("enter the sides of square :"))
s_area=lambda a:a*a
print("the area of square is :",s_area(a))

l=int(input("enter the length of rectangle :"))
b=int(input("enter the breadth of reactangle :"))
r_area=lambda l,b:l*b
print("the area of rectangle is :",r_area(l,b))

b=int(input("enter the base of triangle :"))
h=int(input("enter the height of triangle :"))
t_area=lambda b,h:0.5*b*h
print("the area of triangle is :",t_area(b,h))

