from colorama import Fore, Back, Style

numbers = False; upper = False; eight_char = False; symbols = False

user_pw = input("Senha: ") 

if " " in user_pw: print(Fore.RED + "Sua senha não pode conter espaço :("); print(Style.RESET_ALL), exit()


#checar a presença de números
if user_pw.isalpha() == True: pass
else: numbers = True

#checar a presença de letras maiúsculas
for i in user_pw:

    if i.isupper() == True: upper = True
    else: pass
    
#checar se têm mais de oito caracteres
if len(user_pw) >= 8: eight_char = True
else: pass

#checar se contém símbolos
for j in user_pw:

    if j.isalnum() == True: pass
    else: symbols = True; break

#resultados

if numbers == True: print(Fore.GREEN + "Contém números :)") 
else: print(Fore.RED + "Não contém números :(")

if upper == True: print(Fore.GREEN + "Contém caracteres maiúsculos :)") 
else: print(Fore.RED + "Não contém caracteres maiúsculos :(")

if eight_char == True: print(Fore.GREEN + "Contém oito caracteres ou mais :)") 
else: print(Fore.RED + "Não contém oito caracteres ou mais :(")

if symbols == True: print(Fore.GREEN + "Contém símbolos :)") 
else: print(Fore.RED + "Não contém símbolos :(")

print(Style.RESET_ALL)

