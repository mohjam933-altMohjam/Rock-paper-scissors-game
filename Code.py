import random
r = random.randint(1,3)
u = input("wargeh,mgs,hajara : \n").lower()
if r == 1: 
    print ("wargeh")
elif r == 2:
    print ("mgs")
else:
    print ("hajara")
    
if u == "wargeh" and r == 1: 
    print ("tie")
elif u == "wargeh" and r == 2:
    print ("you win :(")
elif u == "wargeh" and r == 3: 
    print ("you lose >< ;)")
elif u == "mgs" and r == 1 :
    print ("you win :(")
elif u == "mgs" and r == 2 :
    print ("tie")
elif u == "mgs" and r == 3:
    print ("you lose >< ;)")
elif u == "hajara" and r == 1 :
    print ("you lose >< ;)")
elif u == "hajara" and r == 2:
    print ("you win :(")
elif u == "hajara" and r == 3:
    print ("tie")
else:
    print ("""please just enter one of this: "wargeh,mgs,hajara""")
