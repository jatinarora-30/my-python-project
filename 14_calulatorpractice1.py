a=9
b=7
print(f"addition of {a} and {b} is {a+b}")  
print(f"subtration of {a} from  {b} is {a-b}")  
print(f"multiplication of {a} and {b} is {a*b}")  
print(f"division of {a} by {b} is {a/b}")  
print(f"floor division of {a} from {b} is {a//b}")  
print(f"modulus of {a} from {b} is {a%b}")  
print(f"exponentiation of {a} and {b} is {a**b}")  

print()

a=9
b=7
calculations={
    "addition":a+b,
    "subtraction":a-b,
    "multiplication":a*b,
    "division":a/b,
    "modulus":a%b,
    "exponentiation":a**b,
    "floor division":a//b

}
for operation,result in calculations.items():
    print(f"{operation} of {a} and {b} is {result}")