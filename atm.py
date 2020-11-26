class Atm_Card(object):
    def __init__(self, card_no, pin, balance):
        self.card = card_no
        self.pin = pin
        self.balance = balance
    
    def cash_withdrawal(self, card_no, pin, money):
        if self.card == card_no and self.pin == pin:
            if money > self.balance:
                print("You don't have balance to withdraw this amount. You only have:-", self.balance)
            else:
                self.balance -= money
                print("Withdrawed", money, "successfuly. You have", self.balance, "remaining")
        else:
            print("Wrong card no or pin!")

    def balance_enquiry(self, card_no, pin):
        if self.card == card_no and self.pin == pin:
            print("Your Balance is", self.balance)
        else:
            print("Wrong card no or pin!")
    
    def cash_deposit(self, card_no, pin, money_to_deposit):
        if self.card == card_no and self.pin == pin:
            self.balance += money_to_deposit
            print("Successfuly deposited", money_to_deposit, ". You currently have", self.balance)
        else:
            print("Wrong card no or pin!")
    

card_no = input("Enter Card No:- ")
pin = int(input("Enter Pin:- "))
balance = int(input("Enter Balance:- "))

card = Atm_Card(card_no, pin, balance)

while True:
    operation = input("To Withdraw press 'p'. To Deposit press 'd'. To Check Balance press 'b'. To Quit press 'q':- ")

    if operation == "p":
        withdrawal_amount = int(input("Enter Withdrawal Amount:- "))
        card.cash_withdrawal(card_no, pin, withdrawal_amount)
    elif operation == "d":
        deposit_amount = int(input("Enter Deposit Amount:- "))
        card.cash_deposit(card_no, pin, deposit_amount)
    elif operation == "b":
        card.balance_enquiry(card_no, pin)
    elif operation == "q":
        print("Quitting ...")
        break
    else:
        print("operation not found!")
