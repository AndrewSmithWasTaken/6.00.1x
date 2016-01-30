import math

balance = 3926
annualInterestRate = 0.2

guess = balance*1.2

while math.log10((guess/(guess-(annualInterestRate/12)*balance))) / math.log10(1+(annualInterestRate/12)) < 12:
    lastGuess = guess
    guess -= 10
    print 10 - guess%10
    print guess
    x = math.log10((guess/(guess-(annualInterestRate/12)*balance))) / math.log10(1+(annualInterestRate/12))
    if x > 12.00:
        guess = lastGuess - lastGuess%10
        break

print "\nLowest Payment: "+str(int(guess))