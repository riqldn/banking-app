class account:
    account_balance = 0.00
    account_holder = ""

    def withdrawal(self, amount):
        if self.account_balance - amount < 0:
            print("You do not have the sufficient funds to make this transaction")
        else:
            self.account_balance = self.account_balance - amount
            print(
                f"Your withdrawal was successful\nAccount Balance: £{self.account_balance}\n")
            with open("statement.txt", "a") as f:
                f.write(
                    f"Transaction made: Withdrawal\nWithdrawal Amount: {amount}\nCurrent Balance:  £{self.account_balance}\n")
                f.close()

    def deposit(self, amount):
        self.account_balance = self.account_balance + amount
        print(
            f"Your deposit was succesful\nAccount Balance: £{self.account_balance}")
        with open("statement.txt", "a") as f:
            f.write(
                f"Transaction made: Deposit\nDeposit Amount: {amount}\nCurrent Balance: £{self.account_balance}\n")
            f.close()

    def balance(self):
        print(f"Your current Balance is £{self.account_balance}")

    def getname(self):
        self.account_holder = input("May we take your name please?")
        with open("statement.txt", "w") as f:
            f.write(f"{self.account_holder.capitalize()}'s statement\n")
            f.close()

    def statement(self):
        try:
            with open("statement.txt", "r") as f:
                print(f.read())
                f.close()
        except:
            "Your statement wasn't avaliable please try making a statement"


def bank():
    new_account = account()
    print("Welcome to Python Bank")
    new_account.getname()
    userinput = "y"
    while userinput == "y":
        userinput = input(
            "Do you want to make a transaction? Y - yes, N - no\n")
        try:
            userinput = userinput.lower()
        except:
            if userinput != "y" or "n":
                print("incorrect choice\n")
                continue
        userinput = userinput.lower()
        if userinput == "y":
            transaction = True
            while transaction == True:
                transaction_input = input(
                    "Please choose from the following options\n1 - deposit\n2 - withdrawal\n3 - account balance\n4 - print statement\n")
                if int(transaction_input) < 1 or int(transaction_input) > 4:
                    print("INCORRECT CHOICE")
                    continue
                try:
                    transaction_input = int(transaction_input)
                    if transaction_input < 1 and transaction_input > 4 and type(transaction_input) != int:
                        continue
                except:
                    print("INCORRECT VALUE")
                    continue
                if transaction_input == 1:
                    deposit_amount = input(
                        "Please enter the amount you wish to deposit\t")
                    deposit_amount = float(deposit_amount)
                    new_account.deposit(deposit_amount)
                elif transaction_input == 2:
                    withdrawal_amount = input(
                        "Please enter the amount you wish to withdraw\t")
                    withdrawal_amount = float(withdrawal_amount)
                    new_account.withdrawal(withdrawal_amount)
                elif transaction_input == 3:
                    new_account.balance()
                elif transaction_input == 4:
                    new_account.statement()
                userinput = input(
                    "Do you want to make another transaction? Y - yes, N - no\t")
                userinput = userinput.lower()
                if userinput == "y":
                    transaction = True
                elif userinput == "n":
                    transaction = False


bank()
