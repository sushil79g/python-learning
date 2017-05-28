def count(balance, annualInterestRate):
    low = balance / 12;updatedBalance = 1
    monthlyIntrestRate = annualInterestRate / 12.0
    high = (balance * (1 + monthlyIntrestRate) ** 12) / 12.0;a = balance
    while True:
        monthlyFixPayment = round((low + high) / 2, 2)
        updatedBalance = balance
        for x in range(12):
            monthlyUnpaidBalance = updatedBalance - monthlyFixPayment
            updatedBalance = monthlyUnpaidBalance + (monthlyIntrestRate * monthlyUnpaidBalance)
        if round(updatedBalance, 2) > 0:
            low = monthlyFixPayment
        elif round(updatedBalance, 2) < 0:
            high = monthlyFixPayment
        elif round(updatedBalance, 2) == 0: 
            return monthlyFixPayment
        if round(updatedBalance,2)-a==0:
            return monthlyFixPayment
        a = round(updatedBalance,2)
print("Lowest Payment: ", count(balance, annualInterestRate))