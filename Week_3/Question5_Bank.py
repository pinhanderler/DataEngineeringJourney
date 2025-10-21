class Customer:
    def __init__(self, name, surname, tc_identification, phone):
        self.name = name
        self.surname = surname
        self.tc_identification = tc_identification
        self.phone = phone

    def display_information(self):
        print(f"Customer: {self.name} {self.surname}\nTC: {self.tc_identification}\nPhone: {self.phone}")


class Account(Customer):
    def __init__(self, name, surname, tc_identification, phone, account_number, balance=0):
        super().__init__(name, surname, tc_identification, phone)
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} TL deposited successfully. New balance: {self.balance} TL.")

    def money_check(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"{amount} TL withdrawn successfully. Remaining balance: {self.balance} TL.")
        else:
            print("Insufficient balance. Transaction canceled.")

    def display_balance(self):
        print(f"Account Balance: {self.balance} TL")


if __name__ == "__main__":
    acc = Account("Ahmet", "Yılmaz", "12345678910", "05001234567", "TR0001", 5000)
    acc.display_information()
    acc.deposit(1000)
    acc.money_check(2000)
    acc.display_balance()
