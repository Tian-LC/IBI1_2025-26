# input a person's age (in years), weight (in kg), gender, and creatinine	concentration,	Cr,	in	height	(in	µmol/l)
# if age < 100 and weight >	20 and weight < 80 and creatinine	concentration >	0 and creatinine	concentration <	100 and gender = "male"	or "female":
#   if gender is "male":
#        CrCl = ((140-age) * weight) / (72*Cr)
#   else:
#        CrCl = ((140-age) * weight) / (72*Cr) * 0.85
#    print("CrCl is", CrCl)
# else:
#     if age >= 100:
#         print("variable "age" needs corrected")
#     if weight > 80 or weight < 20:
#         print("variable "weight" needs corrected")
#     if Cr <= 0:
#         print("variable "creatinine concentration" needs corrected")
#     if gender neither "male" nor "female":
#         print("variable "gender" needs corrected")
#1. input data
age = float(input("Please input age:"))
weight = float(input("Please input weight:"))
Cr = float(input("Please input creatinine concentration:"))
gender = input("Please input gender:")
#2. check the validity of inputed data
is_valid = True

if age >= 100:
    print("variable 'age' needs to be corrected")
    is_valid = False

if weight <= 20 or weight >= 80:
    print("variable 'weight' needs to be corrected")
    is_valid = False

if Cr <= 0 or Cr >= 100:
    print("variable 'creatinine concentration' needs to be corrected")
    is_valid = False

if gender not in ("male", "female"):
    print("variable 'gender' needs to be corrected")
    is_valid = False

#3. only calculate when the input is valid
if is_valid:
    if gender == "male":
        CrCl = ((140 - age) * weight) / (72 * Cr)
    else:
        CrCl = ((140 - age) * weight) * 0.85 / (72 * Cr)
    print("CrCl is", CrCl)
