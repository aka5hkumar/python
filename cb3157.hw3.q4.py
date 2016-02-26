import turtle
print('Please enter the lengths of 3 sides of a triangle')
a = float(input('Enter the length of the first side: '))
b = float(input('Enter the length of the second side: '))
c = float(input('Enter the length of the third side: '))
if(a == b and a == c):
    print("The sides " + str(a) + ',' + str(b) + ',and ' + str(c) +
          " form an equilateral triangle")
elif((a == b and a != c) or (a == c and a != b) or (c == b and b != a)):
    print("The sides " + str(a) + ',' + str(b) + ',and ' + str(c) +
          " form an isoceles triangle that is not a right triangle")
    if ((a**2 + b**2 == c**2) or (b**2 + c**2 == a**2) or (a**2 + c**2 == b**2)):
        print("The sides " + str(a) + ',' + str(b) + ',and ' + str(c) +
          " form an isoceles triangle that is a right triangle")
else:
    if((a**2 + b**2 == c**2) or (b**2 + c**2 == a**2) or (a**2 + c**2 == b**2)):
        print("The sides " + str(a) + ',' + str(b) + ',and ' + str(c) +
          " form a right triangle")
