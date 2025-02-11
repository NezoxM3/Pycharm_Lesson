from random import randint

class BusinessMan:

    def __init__(self, name):
        self.name = name
        self.money = 1000
        self.energy = 50
        self.motivation = 50
        self.alive = True

    def work(self):
        print("Працюю над бізнесом")
        self.money += randint(500, 2000)
        self.energy -= 5
        self.motivation -= 3

    def invest(self):
        print("Інвестую в нові можливості")
        investment = randint(500, 2000)
        self.money -= investment
        if randint(1, 3) == 1:
            self.money += investment * randint(2, 5)
        else:
            print("Інвестиція не вдалася")

    def relax(self):
        print("Час відпочити")
        self.energy += 5
        self.motivation += 3

    def network(self):
        print("Розширюю коло знайомств")
        self.motivation += 3
        self.energy -= 3

    def is_alive(self):
        if self.money <= 0:
            print("Я збанкрутував")
            self.alive = False
        elif self.energy < 0:
            print("У мене більше немає енергії продовжувати")
            self.alive = False
        elif self.motivation < 0:
            print("У мене більше немає мотивації продовжувати")
            self.alive = False

    def end_of_day(self):
        print(f"Гроші = {self.money}")
        print(f"Енергія = {self.energy}")
        print(f"Мотивація = {self.motivation}")

    def live(self, day):
        print(f"\nДень: {day} - Підприємець: {self.name}")

        action = randint(1, 4)
        if action == 1:
            self.work()
        elif action == 2:
            self.invest()
        elif action == 3:
            self.relax()
        elif action == 4:
            self.network()

        self.end_of_day()
        self.is_alive()


max = BusinessMan("Макс")

for day in range(1, 365):
    if not max.alive:
        break
    max.live(day)

if max.money > 50000:
    print("Вітаю! Ви стали успішним бізнесменом!")

