
for number in [4,9,11]:
     print()
     print(f"\033[1mTABLE OF {number}\033[0m ")
     print()
     for i in range(1,11):
      print(number,"x",i,"=",number*i,)
print()

m=5
n=6
print("----table of",5,"----",  "----table of",6,"----")
for i in range(1,11):
    print(f"  {m} x {i} = {m*i} \t\t{n} x {i} = {n*i}")
    
print()

print("hey my dog's name is \"ELVIN\"",sep="~",end="007")
print("he is a bad man","his name is","jatin",sep="~")

