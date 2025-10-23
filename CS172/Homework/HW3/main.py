from bank import Bank
from accounts import BankAccount, Savings, Checking

def main():
    """Main script to test Bank, Savings, and Checking classes."""
    
    # Create a Bank object
    print("Creating a Bank object...")
    myBank = Bank("First Community Bank")
    print(f"Bank created: {myBank.getBankName()}\n")
    
    # Create a mix of Savings and Checking account objects
    print("Creating Savings accounts...")
    savings1 = Savings("Alice Johnson", 1500.00, 3.5)
    savings2 = Savings("Bob Martinez", 2000.00, 4.0)
    savings3 = Savings("Carol White", 750.00, 3.25)
    savings4 = Savings("David Lee", 3000.00, 4.5)
    
    print("Creating Checking accounts...")
    checking1 = Checking("Emma Brown", 1200.00)
    checking2 = Checking("Frank Wilson", 850.00)
    checking3 = Checking("Grace Taylor", 1500.00)
    checking4 = Checking("Henry Davis", 2200.00)
    print()
    
    # Add several Savings and Checking account objects to the Bank object
    print("Adding accounts to the bank...")
    myBank.addSavings(savings1)
    myBank.addSavings(savings2)
    myBank.addSavings(savings3)
    myBank.addSavings(savings4)
    
    myBank.addChecking(checking1)
    myBank.addChecking(checking2)
    myBank.addChecking(checking3)
    myBank.addChecking(checking4)
    print("All accounts added.\n")
    
    # Remove at least two account objects from the Bank object (one of each type)
    print("Removing accounts from the bank...")
    print(f"Removing Savings account: {savings2.getAccountNumber()} (Bob Martinez)")
    myBank.removeSavings(savings2.getAccountNumber())
    
    print(f"Removing Savings account: {savings4.getAccountNumber()} (David Lee)")
    myBank.removeSavings(savings4.getAccountNumber())
    
    print(f"Removing Checking account: {checking3.getAccountNumber()} (Grace Taylor)")
    myBank.removeChecking(checking3.getAccountNumber())
    
    print(f"Removing Checking account: {checking4.getAccountNumber()} (Henry Davis)")
    myBank.removeChecking(checking4.getAccountNumber())
    print()
    
    # Print the Bank object
    print("="*60)
    print("FINAL BANK STATE")
    print("="*60)
    print(myBank)


if __name__ == "__main__":
    main()