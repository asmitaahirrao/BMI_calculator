# how to calculate BMI
def BMI(height, weight):
	bmi = weight/(height**2)
	return bmi

# Driver code
print("================ BMI Calculator ========================")
print("")
height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kg: "))

# calling the BMI function
bmi = BMI(height, weight)
print("")
print("Your Body Mass Index is: ",bmi)

# Conditions to find out BMI category
if(bmi>0):
    if(bmi<=16):
        print("You are severely underweight..")
    elif(bmi<=18.5):
        print("You are underweight..")
    elif(bmi<=25):
        print("You are healthy..")
    elif(bmi<=30):
        print("You are overweight..")
    else:
        print("You are severely overweight..")
else:
    print("Enter valid details !!")
