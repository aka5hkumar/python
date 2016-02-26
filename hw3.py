#Akash Kumar_ak4341 
#Question 1
#b
print('Enter height and weight in LB')

print('Weight')
weight_lb=float(input())
print ('Height')
height_lb=float(input())


weight=weight_lb*0.453592
#print (weight)
height=height_lb*0.0254
#print (height)

bmi=weight/(height**2)
print ('BMI is: ', bmi)

if (bmi < 18.5):
	print("You are Underweight")
elif(bmi>=18.5 & bmi <25):
	print("You are Normal weight")
elif(bmi>=25 & bmi<30):
	print("You are Overweight")
else:
	print("You are Obese")
