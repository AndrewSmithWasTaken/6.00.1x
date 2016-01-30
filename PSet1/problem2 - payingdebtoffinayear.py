balance = 3329
annualInterestRate = 0.2
guess = 10
workingBalance = balance
while workingBalance > 0:
    for i in range(1,13):
        workingBalance -= guess
        workingBalance *= 1+annualInterestRate/12
        if workingBalance <= 0:
            break
    if workingBalance > 0:
        guess += 10
        workingBalance = balance
print "Lowest Payment: "+str(guess)

