import random 

computer = random.choice(["pedra", "papel", "tesoura"])
user = "banana"

while user not in ["pedra", "papel", "tesoura"]:
    user = input("Escolha entre \"pedra\", \"papel\" ou \"tesoura\": ").lower().strip()

if computer == user:
    print("Computador: {}\n Você: {}\nEmpate!".format(computer,user))
else:

    if computer == "pedra": #pedra
        if user == "tesoura":
            print("Computador: {}\n Você: {}\n Você perdeu!".format(computer,user))
        elif user == "papel":
            print("Computador: {}\n Você: {}\n Você venceu!".format(computer,user))  
    elif computer == "papel": #papel
        if user == "pedra": 
            print("Computador: {}\n Você: {}\n Você perdeu!".format(computer,user))
        elif user == "tesoura":
            print("Computador: {}\n Você: {}\n Você venceu!".format(computer,user))           
    elif computer == "tesoura": #tesoura
        if user == "papel":
            print("Computador: {}\n Você: {}\n Você perdeu!".format(computer,user))
        elif user == "pedra":
            print("Computador: {}\n Você: {}\n Você venceu!".format(computer,user))  
