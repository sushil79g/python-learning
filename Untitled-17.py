def count(balance,annualInterestRate):
 monthlyFixPayment = 0
 updatedBalance = 1
 monthlyIntrestRate = annualInterestRate/12.0
 while updatedBalance > 0:
  monthlyFixPayment += 10
  updatedBalance = balance
  for x in range(12): 
    monthlyUnpaidBalance = updatedBalance - monthlyFixPayment
    updatedBalance = monthlyUnpaidBalance + (monthlyIntrestRate*monthlyUnpaidBalance)
 return monthlyFixPayment 


print("Lowest Payment: ",count(balance,annualInterestRate))