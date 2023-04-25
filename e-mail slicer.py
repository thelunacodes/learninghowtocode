email = input("Insira seu e-mail aqui: ").strip()

username = (email[ : email.index("@")])
print("username: {}".format(username))

domain = (email[(email.index("@") + 1) : ])
print("domain: {}".format(domain))