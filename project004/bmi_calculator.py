weight = float(input("Enter your weight in pounds: "))
height = float(input("Enter your height in cm: "))

bmi = weight / (height ** 2)

# 🚨 Do not modify the values above
# Write your code below 👇
#If the bmi is under 18.5 (not including), print out "underweight"
if bmi < 18.5:
    print("underweight")#
elif 18.5 <= bmi < 25:#If the bmi is between 18.5 (including) and 25 (not including), print out "normal weight"
    print("normal weight")
else:#If the bmi is 25 (including) or over, print out "overweight"
    print("overweight")