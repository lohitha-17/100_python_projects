print("Welcome to Lohi's Pizza!")
size= input("What size pizza you want? S, M or L: \n")
chicken=input("Do you want chicken on your pizza? Y or N: \n")
cheese = input("Do you want cheese on your pizza? Y or N: \n")
bill = 0
if size == "S":
    bill = bill + 9.99
elif size == "M":
    bill = bill + 14.99
elif size == "L":
    bill = bill + 18.99
else:
    print("Please enter a valid size.")

if chicken == "Y":
    if size== "S":
        bill = bill + 2
    elif size== "M":
        bill = bill + 3
    else:
        bill = bill + 4
if cheese == "Y":
    bill = bill + 5
    print("Your total bill is:", bill)
