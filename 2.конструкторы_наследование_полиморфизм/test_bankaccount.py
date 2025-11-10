from bankaccount import BankAccount, Savings, Checking, FixedDeposit

s = Savings(1000, 5, 2)
print("Баланс на сберегательном счете:", s.balance())
print("Проценты:", s.calculate_interest())
print("Итоговый баланс:", s.calculate_balance())

c = Checking(2000, 3, 1, 10)
print("Баланс на расчетном счете:", c.balance())
print("Проценты:", c.calculate_interest())
print("Итоговый баланс:", c.calculate_balance())

fd = FixedDeposit(5000, 7, 3)
print("Основная сумма:", fd.principal())
print("Проценты:", round(fd.calculate_interest(), 2))
print("Итоговый баланс:", round(fd.calculate_balance(), 2))
