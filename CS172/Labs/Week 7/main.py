"""
NAMES AND USERID
Shanielle Hall snh325
Alyn Tetteh    aet78

Date: November 6, 2025
Purpose: Experiment with the Stack data structure and see how some
problems lend themselves well to this data structure.
"""

from stackclass import Stack # imports the stackclass


def postfix(expression):
    #create a stack object
    eqnStack = Stack()
    
    eqnlist = expression.split(" ")
    #splits the expression given by the user
    for i in eqnlist:
        if i.strip("-+").isnumeric():
            eqnStack.push(i)
        else:
            #pop top 2 items from the Stack
            a = float(eqnStack.pop())
            b = float(eqnStack.pop())
            #checks the different operators
            if i == '+': # checks addition
                c = b + a
                eqnStack.push(c)
            elif i == '-': # checks subtraction
                c = b - a
                eqnStack.push(c)
            elif i == '*': # checks multiplication
                c = b * a
                eqnStack.push(c)
            elif i == '/': # checks division
                c = b / a
                eqnStack.push(c) 
    return float(eqnStack.top()) # returns the top of the stack


if __name__ == "__main__":
    """
    print("Testing stack implementation")
    print("----------------------------")
    
    deck = Stack()
    print("empty stack")
    print(deck)
    
    
    deck.push(43)
    deck.push(29)
    deck.push(15)
    print("Testing push method")
    print(deck)
    
    deck.pop()
    print("Testing pop method")
    print(deck)
    
    print("Checking the top of the stack")
    print(deck.top())
    
    print("checking to see if stack is empty")
    print(deck.isEmpty())
    
    print(postfix("4 5 -")) # should print -1.0
    print(postfix("4 9 7 - -")) # should print 2.0
    print(postfix("1 2 3 4 - - -")) # should print -2.0
    print(postfix("1 2 - 3 - 4 -")) # should print -8.0
    print(postfix("15 20 12 + +")) # should print 47.0
    print(postfix("11 2 3 * *")) # should print 66.0
    print(postfix("100 4 2 4 / / /")) # should print 12.5
    print(postfix("4 -1 9 5 2 3 + * - * /")) # should print 0.25
    print(postfix("2 5 + 7 *")) # should print 49.0
    print(postfix("1 2 * 7 + 9 * 11 +")) # should print 92.0
    print(postfix("-1 2 * 7 + -9 * 11 +")) # should print -34.0
    """
    
    print("Welcome to Postfix Calculator")
    print("Enter exit to quit")
    
    expr = ""  
    while expr.lower() != "exit":
        expr = input("Enter Expression\n").strip() #strips the expression entered by the user
        #if the user enters "exit" closes the program
        if expr.lower() != "exit":
            result = postfix(expr)
            print(f"Result: {result}")  
