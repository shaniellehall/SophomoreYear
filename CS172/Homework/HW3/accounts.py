from abc import ABC, abstractmethod #importing the abstract method


class BankAccount(ABC):
    nextAccountNumber = 1000
    
    def __init__(self, owner, balance = 0.0):
        self.__owner = owner
        self.__balance = float(balance)
        self.__accountNumber = BankAccount.nextAccountNumber
        BankAccount.nextAccountNumber += 1
        
    def getOwner(self):
        #returns the name of the owner
        return self.__owner
    
    def getBalance(self):
        #returns the balance of the account
        return self.__balance
    
    def getAccountNumber(self):
        #returns the account number
        return self.__accountNumber
    
    def deposit(self, amount):
        #increase the balance of the account by amount
        self.__balance += float(amount)
        
    def withdraw(self, amount):
        #decrease the balance of the account by amount
        self.__balance -= float(amount)
        
    def __eq__(self, other):
        #compares the bankAccount objects
        try:
            return self.__accountNumber == other.getAccountNumber()
        except AttributeError:
            return False
    
    def __str__(self):
        return (f"Account Number: {self.__accountNumber}\n"
                f"Account Owner: {self.__owner}\n"
                f"Account Balance: ${self.__balance:.2f}")
    
    @staticmethod
    def getNextAccountNumber():
        #returns the next available account number
        return BankAccount.nextAccountNumber
    
    @abstractmethod
    def endOfMonth(self):
        pass
    
class Savings(BankAccount):
    #savings account that earns interest every month

    def __init__(self, owner, balance=0.0, interestRate=3.25):
        #Initialize a Savings account.
        super().__init__(owner, balance)
        self.__interestRate = float(interestRate)
    
    def getInterestRate(self):
        #return the interest rate as a float
        return self.__interestRate
    
    def setInterestRate(self, rate):
        #changes the interest rate to a different value
        self.__interestRate = float(rate)
    
    def __eq__(self, other):
        #compare two Savings objects
        try:
            return self.getAccountNumber() == other.getAccountNumber()
        except AttributeError:
            return False
    
    def __str__(self):
        #return a string of Savings object
        return (f"Account Number: {self.getAccountNumber()}\n"
                f"Account Owner: {self.getOwner()}\n"
                f"Account Balance: ${self.getBalance():.2f}\n"
                f"Annual Interest Rate: {self.__interestRate:.2f}%")
    
    def endOfMonth(self):
        #calculates the interest earned and updates the balance at the end of the month. monthly interest rate = annual rate / 12
        monthly_rate = self.__interestRate / 100 / 12
        interest = self.getBalance() * monthly_rate
        self.deposit(interest)


class Checking(BankAccount):
    #checking account that charges a service fee if transactions exceed 7
    
    def __init__(self, owner, balance=0.0):
        #Initialize a Checking account

        super().__init__(owner, balance)
        self.__transactions = 0
    
    def getTransactionsNum(self):
        #return the current number of transactions
        return self.__transactions
    
    def deposit(self, amount):
        #update transaction count
        super().deposit(amount)
        self.__transactions += 1
    
    def withdraw(self, amount):
        #update transaction count
        super().withdraw(amount)
        self.__transactions += 1
    
    def __eq__(self, other):
        # compares two Checking objects
        try:
            return self.getAccountNumber() == other.getAccountNumber()
        except AttributeError:
            return False
    
    def __str__(self):
        #return a string of Checking object
        return (f"Account Number: {self.getAccountNumber()}\n"
                f"Account Owner: {self.getOwner()}\n"
                f"Account Balance: ${self.getBalance():.2f}\n"
                f"Transactions this month: {self.__transactions}")
    
    def endOfMonth(self):
        #Determines if the service fee ($5.00) needs to be applied. if transactions exceed 7, applies the fee and updates balance. resets the number of transactions to zero.
        if self.__transactions > 7:
            self.withdraw(5.00)
        self.__transactions = 0
