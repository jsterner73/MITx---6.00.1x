balance = 999999
annualInterestRate = 0.18


monthlyInterestRate = annualInterestRate / 12.0
monthlyPaymentLowerBound = balance / 12.0
monthlyPaymentUperBound = (balance * (1 + monthlyInterestRate)**12) / 12.0

lowestPayment = (monthlyPaymentUperBound + monthlyPaymentLowerBound) / 2.0

remain = balance

while remain > 0.01:
    lowestPayment = (monthlyPaymentUperBound + monthlyPaymentLowerBound) / 2.0

    for x in range(1, 13):
        newBalance = remain - lowestPayment
        monthInterest = annualInterestRate/12*newBalance
        remain = newBalance+monthInterest
        
    if (remain < 0):
        monthlyPaymentUperBound = lowestPayment
        remain = balance

    elif (remain > 0.01):
        monthlyPaymentLowerBound = lowestPayment
        remain = balance

print 'Lowest Payment: ' + str(round(lowestPayment, 2))