#saldo = 500
# se for igual ou menor a 500, "saque realizado com sucesso"
#senao "saldo insuficiente"
                        
saldo = 500
saque = int(input(" Digite o saque"))
if saque <= saldo: 
    print (" saque realizado com sucesso")
else: 
    print("saldo insuficiente")