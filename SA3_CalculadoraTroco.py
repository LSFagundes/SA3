from decimal import Decimal
    
compra =  Decimal (input("Valor da compra: "))
pagamento = Decimal (input("Valor pago: "))
troco = pagamento - compra
print("Total do troco: R$", troco)
print("Você deve entregar ao cliente:")
ced = Decimal(100)
TotalCedulas = Decimal(0)
while True:
    if troco >= ced:
        troco -= ced
        TotalCedulas += 1
    elif  compra == pagamento: 
            print("Não precisa de troco")
            break
    else:
        if ced > 1 and TotalCedulas > 0:
            print(TotalCedulas, "cédula(s) de R$", ced)
        if ced <=1 and TotalCedulas > 0:
             print (TotalCedulas, "moeda(s) de R$ ", ced)
        if ced == 100.:
            ced = Decimal(50)
        if ced == 50:
             ced = Decimal(20)
        elif ced == 20:
             ced = Decimal(10)
        elif ced == 10:
             ced = Decimal(2)
        elif ced == 2:
             ced = Decimal(1)
        elif ced == 1:
             ced = Decimal(0.5)
        elif ced == 0.5:
             ced = Decimal('0.05')
        TotalCedulas = 0
        if troco == 0:
            break
        
    
    
   
   

        

    

