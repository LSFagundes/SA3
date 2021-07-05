#from decimal import Decimal
#compra =  Decimal (input("Valor da compra: "))
#pagamento = float (input("Valor pago: "))
#ganhos = pagamento + compra

m_d = {100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 1: 0, 0.25: 0, 0.1: 0, 0.05: 0, 0.01: 0}
# list of possible bills/coins, really only used in the for loop later on
m_l = [100, 50, 20, 10, 5, 1, 0.25, 0.1, 0.05, 0.01]
cost = float(input("Cost of item: "))
paid = float(input("Money paid:   "))
if paid < cost:
    print ("You have not paid enough")
else:
    change = paid - cost
    print ("Change: $", change)
    for i in m_l:
        while change >= i:
            m_d[i] += 1
            change -= i

    print ("100's:"),m_d[100]
    print (" 50's:"),m_d[50]
    print (" 20's:"),m_d[20]
    print (" 10's:"),m_d[10]
    print ("  5's:"),m_d[5]
    print ("  1's:"),m_d[1]
    print ("  Q's:"),m_d[0.25]
    print ("  D's:"),m_d[0.1]
    print ("  N's:"),m_d[0.05]
    print ("  P's:"),m_d[0.01]