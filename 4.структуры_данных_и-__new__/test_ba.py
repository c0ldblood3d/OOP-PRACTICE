from BankAccount import BankAccount

account = BankAccount()
account.deposit(1000)
account.deposit(500)
print("Баланс после пополнений:", account.get_balance())
account.withdraw(300)
print("Баланс после снятия 300:", account.get_balance())
account.withdraw(200)
print("Окончательный баланс:", account.get_balance())
