class Bank:
        #Bank class to manage Savings and Checking accounts
    
    def __init__(self, bankName):
        
        #initialize a Bank with bankName
        self.__bankName = bankName
        self.__savings = []
        self.__checking = []
    
    def getBankName(self):
        #returns the name of the bank
        return self.__bankName
    
    def getSavings(self):
        #returns the savings account
        return self.__savings
    
    def getChecking(self):
        #returns the checking account
        return self.__checking
    
    def addSavings(self, account):
        #adds a Savings account to the bank
        try:
            if account.__class__.__name__ == 'Savings':
                if account not in self.__savings:
                    self.__savings.append(account)
        except AttributeError:
            pass
    
    def addChecking(self, account):
        #adds a Checking account to the bank
        try:
            if account.__class__.__name__ == 'Checking':
                if account not in self.__checking:
                    self.__checking.append(account)
        except AttributeError:
            pass
    
    def removeSavings(self, accountNumber):
        #remove a Savings account from the bank by account number
        for account in self.__savings:
            if account.getAccountNumber() == accountNumber:
                self.__savings.remove(account)
                return
    
    def removeChecking(self, accountNumber):
        #remove a Checking account from the bank by account number.
        for account in self.__checking:
            if account.getAccountNumber() == accountNumber:
                self.__checking.remove(account)
                return
    
    def __str__(self):
        #returns a string representation of the Bank object
        result = f"{self.__bankName}\n"
        result += f"Savings Accounts\n\n"
        for account in self.__savings:
            result += f"{account}\n\n"
        
        result += f"Checking Accounts\n\n"
        for account in self.__checking:
            result += f"{account}\n\n"
        
        return result.rstrip()