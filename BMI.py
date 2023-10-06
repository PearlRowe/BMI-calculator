height=float(input ("enter your height"))
weight=float(input("enter your weight"))
BMI=weight/(height)*2
print("Your BMI is :" ,BMI)
if BMI <=18.5:
  print("Underweight")
elif BMI <=24:
  print ("normal")
  else BMI <=29.9:
  print("overweight")
