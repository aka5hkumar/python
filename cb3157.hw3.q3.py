print('Please input 3 values for the equation ax^2 +bx + c')
a = float(input('Enter value for a: '))
b = float(input('Enter value for b: '))
c = float(input('Enter value for c: '))
discriminant = b**2 - 4*a*c
root1 = -b / 2*a
#In calculus, the discriminant this tells us of nature of quadratic roots
if (a == 0 and b == 0 and c == 0):
    print('There are infinitely many solutions to this equation')
elif (a == 0 and b == 0 and c != 0):
      print('There are no solutions')
if (discriminant == 0):
    print("This quadratic equation has 1 solution and this solution is x =", root1)
elif (discriminant > 0):
      print('This equation has 2 real roots')
elif (discriminant < 1):
      print('This equation has no real roots')

      
