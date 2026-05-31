print()
a=input("what is your name: ")
len1=len(a)
if len(a) > 12:
   print(f" yes,the lenght of len(a) is = {len(a)}")
else:
   print(f" no ,the lenght of len(a) is ={len(a)}")

print()
abc=[{    
       "name":"jatin",
       "surname":"arora",
                },
     {
            "name":"ashish",
            "surname":"chanchlani",
           } ,
]
print(f"-name of 1st student\t -name of 2nd student ")
dict1=abc[0]
dict2=abc[1]
print(f"name : {dict1["name"]}\t\t name :{dict2["name"]}")
print(f"surname : {dict1["surname"]}\t\t surname :{dict2["surname"]}")

print()
abc=[{    
       "name":"arush",
       "surname":"mighlani",
                },
     {
         "name":"ronak",
         "surname":"bansal",
           } ,
]
print(f"-name of 3rd student\t -name of 4th student ")
dict1=abc[0]
dict2=abc[1]
print(f"name : {dict1["name"]}\t\t name :{dict2["name"]}")
print(f"surname : {dict1["surname"]}\t surname :{dict2["surname"]}")

print()

asf=[ {
       "game":"free fire",
       "release date":2006,

        },
    {
        "game":"bgmi",
        "release date":2005,

    },
]
print(f" name of 1st game:\t name of 2nd game :")
dict5=asf[0]
dict6=asf[1]
print(f" game: {dict5['game']}\t game: {dict6['game']}")
print(f" release date: {dict5['release date']}\t release date: {dict6['release date']}")
