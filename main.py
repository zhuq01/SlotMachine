MAX_LINES = 3

def deposit():
    while True:     #continuously ask user a deposit amount until a valid number is given 
        amount = input("What would you like to deposit? $")
        if amount.isdigit():        #if amount input is a valid whole number
            amount = int(amount)    #covert to a number
            if amount > 0:          #check if amount is greater than 0
                break               #if amount > 0 we break and return amomunt
            else:                   
                print("Amount must be greater than 0.")     #we ask again for a correct input
        else:
            print("Please enter a number: ")                #input from user
    return amount

def get_number_of_lines():
    while True:     
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():        
            lines = int(lines)    
            if 1 <= lines <= MAX_LINES:          
                break               
            else:                   
                print("Enter a valid number of lines")     
        else:
            print("Please enter a number: ")               
    return lines


def main():
    balance = deposit()
    lines = get_number_of_lines()
    print(balance, lines)

main()