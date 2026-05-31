a=2
b=3
print(int(a)+int(b))

a=(input("enter ur 1 number:"))
b=(input("enter ur 2 number: "))
adc={
    "addition":f"addition of {a} and {b} is {int(a)+int(b)}",
    "subtraction":f"subtraction of {a} and {b} is {int(a)-int(b)}",
    "multiplication":f"multiplication of {a} and {b} is {int(a)*int(b)}",
    "division":f"division of {a} from {b} is {int(a)/int(b)}",
    "modulus":f"modulus of {a} from {b} is {int(a)%int(b)}",
    "floor division":f"floor division of {a} from {b} is {int(a)//int(b)}",
}

for operation,result in adc.items():
    print(f"{operation} of {a} and {b} is {result}")


