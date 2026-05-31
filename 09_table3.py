

list=[3,4] 
print()
print(f"\t---TABLE OF 3---\t---TABLE OF 4---")
print()
for i in range (1,12,1):
    print(f"\t{list[0]} x {i} = {list[0]*i} \t\t{list[1]} x {i} = {list[1]*i}")

list=[3,4]
print()
print(f"\t---TABLE OF 3---\t---TABLE OF 4---")
print()
for i in range (11,0,-1):
    print(f"\t{list[0]} x {i} = {list[0]*i} \t\t{list[1]} x {i} = {list[1]*i}")

for number in [3,4,5]:
 print()
 print(f" ---TABLE OF {number}---")
 print()
 for i in range (11,0,-1):
    print(f" {number} x {i} = {number*i}")