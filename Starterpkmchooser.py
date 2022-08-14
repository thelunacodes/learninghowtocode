import random

#Coded by TheLuna (delunatriestocode on github)

gen1 = ["Bulbasaur","Charmander","Squirtle"]
gen2 = ["Chikorita","Cyndaquil","Totodile"]
gen3 = ["Treecko","Torchic","Mudkip"]
gen4 = ["Turtwig","Chimchar","Piplup"]
gen5 = ["Snivy","Tepig","Oshawott"]
gen6 = ["Chespin","Fennekin","Froakie"]
gen7 = ["Rowlet","Litten","Popplio"]
gen8 = ["Grookey","Scorbunny","Sobble"]
gen9 = ["Sprigatito","Fuecoco","Quaxly"]

userchoice = -1
validchoices = [1,2,3,4,5,6,7,8,9]


while userchoice not in validchoices:
    userchoice = int(input("Qual geração? (Insira um número de 1 à 9): "))

if userchoice == 1:
    print("Seu inicial na gen 1 será: {}".format(random.choice(gen1)))   

elif userchoice == 2:
    print("Seu inicial na gen 2 será: {}".format(random.choice(gen2))) 

elif userchoice == 3:
    print("Seu inicial na gen 3 será: {}".format(random.choice(gen3)))     

elif userchoice == 4:
    print("Seu inicial na gen 4 será: {}".format(random.choice(gen4)))     

elif userchoice == 5:
    print("Seu inicial na gen 5 será: {}".format(random.choice(gen5))) 

elif userchoice == 6:
    print("Seu inicial na gen 6 será: {}".format(random.choice(gen6))) 

elif userchoice == 7:
    print("Seu inicial na gen 7 será: {}".format(random.choice(gen7))) 

elif userchoice == 8:
    print("Seu inicial na gen 8 será: {}".format(random.choice(gen8)))         

elif userchoice == 9:
    print("Seu inicial na gen 9 será: {}".format(random.choice(gen9))) 