size=(input("whats size you wanr"))
bill=0
if(size=='S' or size=='s'):
    bill+=100
    print("small pizza price is 100")
elif(size=='M' or size=='m'):
    bill+=200
    print("medium pizza price 200")
else:
    bill+=300
    print("large pizza price 300")
add_pepperoni=input("do you want pepperoni(y/n)? ")
if(add_pepperoni=='Y' or add_pepperoni=='y'):
    if(size=='S'or size=='s'):
        bill+=30
    else:
        bill+=50
extra_cheej=input("do you want extra cheej(y/n)")
if(extra_cheej=='Y' or extra_cheej=='y'):
    bill+=20
    print(f"your final bill is {bill}")
                
        
        
    
    
    
    
    
    
    
    
    
    