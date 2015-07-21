balance = 4842
annualInterestRate = 0.2
monthlyPaymentRate = 0.04


monthlyInterestRate = annualInterestRate / 12.0
totalPaid = 0
previousBalance = balance

for x in range(1,13):
    minimumMonthlyPayment = monthlyPaymentRate * previousBalance
    monthlyUnpaidBalance = previousBalance - minimumMonthlyPayment
    previousBalance = monthlyUnpaidBalance + (monthlyInterestRate * monthlyUnpaidBalance)
    totalPaid += minimumMonthlyPayment
    print 'Month: ' + str(x)
    print 'Minimum monthly payment: ' + str(round(minimumMonthlyPayment, 2))
    print 'Remaining balance: ' + str(round(previousBalance, 2))
    
print 'Total paid: ' + str(round(totalPaid, 2))
print 'Remaining balance: ' + str(round(previousBalance, 2))
