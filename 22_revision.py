a=7
b=10
print(f"multiplication  of {a} and {b} is {a*b}")
print(f"division  of {a} from {b} is {a/b}")
print(f"subtraction  of {a} and {b} is {a-b}")
print(f"addition  of {a} and {b} is {a+b}")
print(f"modulus   of {a} from {b} is {a%b}")
print(f"floor division of {a} from {b} is {a//b}")


print()

a=7
b=10
cdc={
     "addition":a+b,
     "subtraction":a-b,
     "division":a/b,
     "floor division":a//b,
     "modulus":a%b,
     "multiplication":a*b,
     "exponential":a**b,
}

for operations,results in cdc.items():
     print(f"{operations} of {a} and {b} is {results}") 

print()

m=11
n=7
print()
print(f" ---table of {m}--- ---table of {n}")
print()
for i in range(1,11):
  print(f"{m} x {i} = {m*i} \t----{n} x {i} = {n*i}")

print()

m=5
n=6
print()
print(f" ---table of {m}--- ---table of {n}")
print()
for i in range(1,11):
  print(f"{m} x {i} = {m*i} \t----{n} x {i} = {n*i}")

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

print()


a=int(input("enter ur 1 number:"))
b=int(input("enter ur 2 number: "))
adc={
    "addition":f"addition of {a} and {b} is {a+b}",
    "subtraction":f"subtraction of {a} and {b} is {a-b}",
    "multiplication":f"multiplication of {a} and {b} is {a*b}",
    "division":f"division of {a} from {b} is {a/b}",
    "modulus":f"modulus of {a} from {b} is {a%b}",
    "floor division":f"floor division of {a} from {b} is {a//b}",
}  

for operation,result in adc.items():
    print(f"{operation} of {a} and {b} is {result}")
    
print()

a=(input("enter ur name:"))
b=(input("enter ur surname: "))
aa={
    "name": a,
    "surname":b,

}

for key,values in aa.items():
   print(f" {key} : {values}")