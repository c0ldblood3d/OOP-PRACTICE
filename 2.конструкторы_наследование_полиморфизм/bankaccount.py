from abc import ABC, abstractmethod
import math

class BankAccount(ABC):
    @abstractmethod
    def calculate_interest(self):
        pass
    
    @abstractmethod
    def calculate_balance(self):
        pass

class Savings(BankAccount):
    def __init__(self, balance, rate, time):
        self.__balance = balance
        self.__rate = rate
        self.__time = time
    
    def balance(self):
        return self.__balance
    
    def rate(self):
        return self.__rate
    
    def time(self):
        return self.__time
    
    def calculate_interest(self):
        return self.__balance * self.__rate * self.__time / 100
    
    def calculate_balance(self):
        interest = self.calculate_interest()
        return self.__balance + interest

class Checking(BankAccount):
    def __init__(self, balance, rate, time, fee):
        self.__balance = balance
        self.__rate = rate
        self.__time = time
        self.__fee = fee
    
    def balance(self):
        return self.__balance
    
    def rate(self):
        return self.__rate
    
    def time(self):
        return self.__time

    def fee(self):
        return self.__fee
    
    def calculate_interest(self):
        return self.__balance * self.__rate * self.__time / 100 - self.__fee
    
    def calculate_balance(self):
        interest = self.calculate_interest()
        return self.__balance + interest

class FixedDeposit(BankAccount):
    def __init__(self, principal, rate, time):
        self.__principal = principal
        self.__rate = rate
        self.__time = time
    
    def principal(self):
        return self.__principal
    
    def rate(self):
        return self.__rate
    
    def time(self):
        return self.__time
    
    def calculate_balance(self):
        return self.__principal * math.pow(1 + self.__rate / 100, self.__time)
    
    def calculate_interest(self):
        final_balance = self.calculate_balance()
        return final_balance - self.__principal