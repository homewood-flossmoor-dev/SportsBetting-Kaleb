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
        print("Hi,"+ self.username+ " you have a total of :" + str(self.money))
    def pay_money(self,money,username):
        self.money -= money
        for user in users_list:
            if user.username == username:
                user.money += money
        
        print(self.username + " you have payed: " + str(money) + " dollars to " + username)

juan = Person("Juan","1234",400)
kaleb = Person("Kaleb", "1234", 500)
users_list = [juan, kaleb]
kaleb.print_payed()
juan.print_payed()
print("------")
juan.pay_money(200, "Kaleb")
print("------")
kaleb.print_payed()
juan.print_payed()

class Match:
    def __init__(self, teams, score, players, updates, time, overtime, fouls):
        self.teams = teams
        self.score = score
        self.players = players
        self.updates = updates
        self.time = time
        self.overtime = overtime
        self.fouls = fouls
