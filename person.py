class Person:
    def __init__(self, username,password,money):
        self.username = username
        self.password = password
        self.money = money        

    def add_money(self, money):
        self.money += money
        print("You have added: " + str(money) + " to your account")
    def substract_money(self,money):
        self.money -= money
        print("You have substracted: " + str(money) + " from your account")
    def print_payed(self):
        print("You payed: " + str(self.money))

person = Person("Juan","1234",100)
person.add_money(money=100)
person.substract_money(money=50)
person.print_payed()