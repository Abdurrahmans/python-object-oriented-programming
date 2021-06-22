class User:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def show_details(self):
        print('User Details: ')
        print('Name: {0} Age: {1} Gender: {2}'.format(self.name, self.age, self.gender))



class Bank(User):
    def __init__(self, name, age, gender):
        super(Bank, self).__init__(name, age, gender)
        self.balance = 0

    def deposit(self, amount):
        self.amount = amount
        self.balance = self.balance + amount
        print('Account balance has been  updated $:', self.balance)

    def withdraw(self, amount):
        if self.balance < amount:
            print('insufficient Funds | Balance Available', self.balance)
        else:
            self.balance = self.balance - amount
            print('Account balance has been  updated $:', self.balance)

    def show_balance(self):
        self.show_details()


user = Bank('Abdur', 24, 'Male')
user.deposit(200)
user.deposit(500)
user.withdraw(300)
user.withdraw(600)
user.show_balance()
