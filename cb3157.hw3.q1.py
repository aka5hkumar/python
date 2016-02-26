weight = float(input('Please enter your weight in kilograms '))
height = float((input('Please enter your height in meters ')))
bmi = weight / height
if (bmi < 18.5):
    print('You are underweight')
elif (bmi <= 24.9 and bmi >= 18.5):
    print('You are normal') 
elif (bmi >= 25.0 and bmi <= 29.9):
    print('You are overweight')
elif (bmi >= 30):
    print('You are obese')
          
