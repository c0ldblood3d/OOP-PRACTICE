class OnlineBank:
    def __init__(self):
        self.accounts = {}

    def register_account(self, id, start_balance):
        if id in self.accounts:
            print('ID занят!')
            return False 
        else:
            self.accounts[id] = start_balance
            print(f'Счет {id} создан с балансом {start_balance}')
            return True

    def deposit_funds(self, id, amount):
        if id not in self.accounts:
            print('Ошибка: Счет не существует!')
            return False
            
        self.accounts[id] += amount
        return True

    def withdraw_funds(self, id, amount):
        if id not in self.accounts:
            print('Ошибка: Счет не существует!')
            return False
             
        if self.accounts[id] < amount:
            print('Ошибка: Недостаточно средств!')
            return False
            
        self.accounts[id] -= amount
        return True
    
    def check_current_balance(self, id):
        if id not in self.accounts:
            print('Счета не существует!')
            return None 
            
        balance = self.accounts[id]
        print(f'Баланс счета {id}: {balance}')
        return balance