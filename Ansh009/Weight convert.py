


weight = float(input("Enter your weight:- "))
unit = input("Kilograms or Pounds?(K or P):- ")
if unit == "K":
    weight = weight * 2.205
    unit = "Lbs"
    print(f"Yor weight is : {round(weight, 1)} {unit}")
elif unit == "P":
    weight = weight / 2.205
    unit = "Kgs"
    print(f"Yor weight is : {round(weight, 1)} {unit}")
else:
    print(f"{unit} Was not valid")
    
    
    
    
    
