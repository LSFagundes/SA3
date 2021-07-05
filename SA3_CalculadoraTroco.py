from decimal import Decimal
    
compra =  Decimal (input("Valor Total das Compras: "))
pagamento = Decimal (input("Valor Recebido: "))
troco = pagamento - compra
print("Troco: R$", troco)
print("Você deve entregar ao cliente:")
ced = Decimal('100.00')
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
            print(TotalCedulas, "Nota(s): R$", ced)
        if ced <=1 and TotalCedulas > 0:
             print (TotalCedulas, "Moeda(s): R$ ", ced)
        if ced == 100.00:
           ced = Decimal('50.00')
        if ced == 50.00:
             ced = Decimal('20.00')
        elif ced == 20.00:
             ced = Decimal('10.00')
        elif ced == 10.00:
             ced = Decimal('2.00')
        elif ced == 2.00:
             ced = Decimal('1.00')
        elif ced == 1.00:
             ced = Decimal('0.50')
        elif ced == 0.50:
             ced = Decimal('0.05')
        TotalCedulas = 0
        if troco == 0:
            break
        
    
    
   
   

        

    

