balance = 4213
annualInterestRate = .2
monthlyPaymentRate = .04
totalPaid = 0

for i in range(1,13):
    print "Month: "+str(i)
    print "Minimum monthly payment: "+str(round(monthlyPaymentRate*balance, 2))
    totalPaid += round(monthlyPaymentRate*balance, 2)
    balance -= round(monthlyPaymentRate*balance, 2)
    balance += round(annualInterestRate/12*balance, 2)
    print "Remaining balance: "+str(round(balance, 2))   
print "Total paid: "+str(round(totalPaid, 2))
print "Remaining balance: "+str(round(balance, 2))