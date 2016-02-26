#Problem 2
uno=int(input("Enter one integer "))
two=int(input("Enter another "))
if (uno>=0 and two>=0):
	quad = 1
elif (uno>=0 and two<0):
	quad = 2
elif (uno<0 and two<0):
	quad = 3
elif (uno<0 and two>=0):
	quad = 4
print("Quadrant = ", quad)

#Problem 3
add=str(input("Enter two integers seperated by a space "))

space=add.find(" ")

int1 = int(add[:space])
int2 = int(add[space+1:])

answer = int1+int2
str2 = str(int1)+'+'+str(int2)+'='+str(answer)
print (str2)
#Problem 4
import turtle
color = str(input("Enter a color: "))
shape = str(input("Enter a shape: "))
size = int(input("Enter a size: "))

turtle.color(color)
turtle.shape(shape)
turtle.shapesize(size,size)
#Problem 5
old_tel=str(input("Please enter the old phone number "))
if(old_tel[3]!= '-' and old_tel[7]!='-' and len(old_tel)==12):
    print ("invalid number")
else:
    save= old_tel[8:]
    new_tel = str(('646-997-')+save)
    print (new_tel)

#Question 6
phrase=str(input("enter the phrase: "))
first_space = phrase.find(" ")
small_phrase=phrase[1+first_space:]
second_space= small_phrase.find(" ")
second_space+=first_space+1
print (phrase[0],phrase[first_space+1],phrase[second_space+1])

caps=str(input("enter a word: "))
caps = caps.upper()
print (caps)

#Question 7
num=int(input("Enter an integer: "))

n=0
while (2**n <= num):
	n += 1
power = n-1
print ("the largest power less than", num, "is ", 2**power, "its exponent is", power)

