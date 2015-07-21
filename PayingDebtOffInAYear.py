balance = 3926
annualInterestRate = 0.2


lowestPayment = 10

while True:
    monthlyInterestRate = annualInterestRate / 12.0
    totalPaid = 0
    previousBalance = balance
    
    for x in range(1,13):
        monthlyUnpaidBalance = previousBalance - lowestPayment
        previousBalance = monthlyUnpaidBalance + (monthlyInterestRate * monthlyUnpaidBalance)
        totalPaid += lowestPayment
    
    if previousBalance > 0:
        lowestPayment += 10
    else:
        break
    
print 'Lowest Payment: ' + str(lowestPayment)