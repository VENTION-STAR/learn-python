import math
a =1
b =8
c =3
delta = b*b-4*a*c
print(delta)
root_1 = ((-b)+math.sqrt(delta))/(2*a)
root_2 = ((-b)-math.sqrt(delta))/(2*a)
print(str(root_1)+'和'+str(root_2))