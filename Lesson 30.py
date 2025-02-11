from random import randint

class Astronaut:

    def __init__(self, name):
        self.name = name
        self.health = 100
        self.energy = 50
        self.morale = 50
        self.alive = True

    def to_explore(self):
        print("Досліджую територію")
        self.morale += 0.8
        self.energy -= 4

    def to_repair(self):
        print("Ремонт бази!!!")
        self.energy -= 2
        self.morale -= 2

    def to_rest(self):
        print("Час відпочити")
        self.energy += 5
        self.morale += 0.8

    def to_communicate(self):
        print("Зв'язався із землею")
        self.energy -= 2
        self.morale += 2


    def is_alive(self):
        if self.health <= 0:
            print("Здоров'я підвело")
            self.alive = False

        elif self.energy <= 0:
            print("У мене більше немає енергії продовужвати")
            self.alive = False

        elif self.morale <= 0:
            print("У мене більше немає сенсу продовужвати")
            self.alive = False


    def end_of_day(self):
        print(f"Здоров'я = {self.health}")
        print(f"Енергія = {self.energy}")
        print(f"Мораль = {self.morale}")

    def live(self, day):
        print(f"День: {day} - Космонавт: {self.name}")

        live_cube = randint(1,4)

        if live_cube == 1:
            self.to_explore()

        if live_cube == 2:
            self.to_repair()

        if live_cube == 3:
            self.to_rest()

        if live_cube == 4:
            self.to_communicate()

        self.end_of_day()
        self.is_alive()


max = Astronaut("Max")

for day in range(1, 365):
    if max.alive == False:
        break

    max.live(day)
