print(f" multiplication table of 2")
print() 
for i in range (1,11):
    print(f" 2 x {i} = {2*i}")
print()
print(f" addition of 5")
print()
for m in range(1,5):
        print(f" 5 + {m} = {5+m}")
print()
print(f" reverse table of 2")      
print()
for i in range(11,0,-1):
    print(f" 2 x {i} = {2*i}")
print()
print(f" addiition of 4 in i ")
print()
for i in range (1,8):
   print(f" 4 + {i} = {4+i}")

print()

a=(input(f"enter your class: "))
b=(input(f"enter your roll_no."))
group={
       "class": a,
       "roll_no.":int(b),

}

for key,values in group.items():
     print(f" {key} : {values}")

print()

m=input( "enter the value of m= ")
n=input( "enter the value of n= ")
if m>n:
      print(f" your answer is true")
else:
     print(f" no your answer is not true")

print()

x=int(input( "enter the value of x= "))
y=int(input( "enter the value of y= "))
if x>y:
    aas={
        "addition":x+y,
        "subtraction":x-y

    }
    for key,values in aas.items():
     print(f" {key} : {values}")

else:
    for i in [2,3]:
        print(f" {x} x {i} = {x**y* i}")

print()        

m=int(input( "enter the value of m= "))
n=int(input( "enter the value of n= "))


if m>n:
    aas={
        "food":"pizaa",
        "pasta":"white sauce",

    }
    for key,values in aas.items():
        print(f" {key} : {values}")

else:
    adc={
        "cold-drink1":"coca cola",
        "cold_drink2":"pepsi",
    }
    
    for key,values in adc.items():
       print(f" {key} : {values}")

print()

m=int(input(f" ENTER YOUR BIRTHDATE : "))
n=int(input(f" ENTER YOUR BIRTHYEAR:   "))
if m<n: 
        fr={
                  "BIRTHDATE": m,
                  "BIRTHYEAR": n,
                
        }        
        for key,value in fr.items():  
          print(f" {key} :{value}")

else:
       
       print(f"\t----TABLE OF {m}----\t----TABLE of {n} ----")
       for i in range (10,0,-1):
                print(f"\t 2 x {m} = {2*m} \t\t 2 x {n} = {2*n}")

print()

for m in [3,8]:
    print()
    print(f" \033[1m table of {m}\033[0m ") 
    print()
    for i in range(1,11):
     print(f" {m} x {i} = {m*i} ")