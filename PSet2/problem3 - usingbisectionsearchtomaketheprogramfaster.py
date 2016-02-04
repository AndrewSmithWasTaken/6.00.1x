balance = 100000
annualInterestRate = .043
interest = annualInterestRate / 12
lo = balance / 12.00
hi = (balance * (1 + interest)**12) / 12.00
guess = (hi+lo) / 2.00
margin = 0.01
workingBalance = balance
while workingBalance > margin:
    for i in range(1,13):
        workingBalance -= guess
        workingBalance *= 1+annualInterestRate/12.00
    if workingBalance > -margin and workingBalance < margin:
        print "Lowest Payment: "+str(round(guess, 2))
    elif workingBalance > 0:
        lo = guess
        guess = (hi+lo) / 2.00
        workingBalance = balance
    elif workingBalance < 0:
        hi = guess
        guess = (hi+lo) / 2.00
        workingBalance = balance
