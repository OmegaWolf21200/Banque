from random import randint
from time import sleep


Game_on = True 
Money = 1000
Chest = 1
Chest_time = 0
Client = 0
Chest_Iron = 1
Chest_Gold = 0

while Game_on :
    commande = input ("Saisisez votre commande ")
    if commande == "Buy_chest" :
        Money -= 1000
        Chest += 1
    elif commande == "Money" :
        print ("Vous avez", Money, "$" )
        continue
    elif commande == "Quit" :
        Game_on = False
    elif commande == "Client" :
        print (Client)
        continue 
    elif commande == "Buy_Chest_Gold" :
        Money -= 7000
        Chest_Gold += 1
    elif commande == "Number_chest_gold" :
        print (Chest_Gold)
        continue
    elif commande == "Number_chest_iron" :
        print (Chest_Iron)
        continue 
    elif commande == "Number_chest" :
        print (Chest)
        continue 
    
    
    client1 = randint(1,Chest)
    sleep(1)
    Money += (Chest_Iron*100)+(Chest_Gold*200)
    Client += client1
    Luck = randint (0,2)  
    if Luck == 0 :
        Money -= Client*5
    else :
        Money += Client*5 