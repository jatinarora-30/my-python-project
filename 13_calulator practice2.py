a=9
b=2
adc={
    "addition":a+b,
    "subtraction":a-b,
    "division":a/b,
    "floor division":a//b,
    "modulus":a%b,
    "exponentiation":a**b,
    "multiplication":a*b,
} 
for operation,result in adc.items():
    print(f"{operation} of {a} and {b} is {result}")

print()


a=9
b=7
operations = ["addition", "subtraction", "multiplication", "division", "modulus", "exponentiation", "floor division",
              "addition", "subtraction"]
results = [a+b, a-b, a*b, a/b, a%b, a**b, a//b,a+b,a-b]
for i in range(0,9):
    print(f"{operations[i]} of {a} and {b} is {results[i]}")