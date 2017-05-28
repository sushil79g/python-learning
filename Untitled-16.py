# Paste your code into this box
def credit(balance,annualInterestRate,monthlyPaymentRate):
  month = 1
  while month<=12:
    minimumPayment = monthlyPaymentRate*balance
    unpaidBalance = balance - minimumPayment
    interest = annualInterestRate*unpaidBalance/12.0
    balance = unpaidBalance + interest
    month +=1 
  return round(balance,2)  


print("Remaining balance:",credit(balance,annualInterestRate,monthlyPaymentRate))

