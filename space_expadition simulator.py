from random import randint, choice


class Astronaut:

    def __init__(self, name, spaceship = None):
        self.name = name
        self.oxygen = 100
        self.energy = 100
        self.inventory = []
        self.spaceship = spaceship

    def mine_resources(self):
        self.home = House()

    def get_car(self):
        self.car = Auto(brands_of_car)

    def get_job(self):

        if self.car.drive():
            pass
        else:
            self.to_repair()
            return

        self.job = Job(job_list)

    def eat(self):

        if self.home.food <= 0:
            self.shopping("food")

        else:
            if self.satiety >= 100:
                self.satiety = 100
                return

            self.satiety += 5
            self.home.food -= 5

    def work(self):
        if self.car.drive():
            pass

        else:

            if self.car.fuel < 20:
                self.shopping("fuel")
                return

            else:
                self.to_repair()

        self.money += self.job.salary
        self.gladness -= self.job.gladness_less
        self.satiety -= 4

    def shopping(self, manage):
        if self.car.drive():
            pass

        else:
            if self.car.fuel < 20:
                manage = "fuel"

            else:
                self.to_repair()
                return

        if manage == "fuel":
            print("I bought fuel")
            self.money -= 100
            self.car.fuel += 100

        elif manage == "food":
            print("Bought food")
            self.money -= 50
            self.home.food += 50

        elif manage == "delicasies":
            print("Hooray! delicious!")
            self.gladness += 10
            self.satiety += 2
            self.money -= 15

    def chill(self):
        self.gladness += 10
        self.home.mess += 5

    def clean_home(self):
        self.gladness -= 5
        self.home.mess = 0

    def to_repair(self):
        self.car.strength += 100
        self.money -= 50

    def day_info(self, day):
        print(f"Today the {day} of {self.name}'s life")
        print(f"Money - {self.money}")
        print(f"Satiety - {self.satiety}")
        print(f"Gladness - {self.gladness}")
        print(f"Food in home - {self.home.food}")
        print(f"Mess in home - {self.home.mess}")
        print(f"Car fuel - {self.car.fuel}")
        print(f"Car strength - {self.car.strength}")
        print("\n")

    def is_alive(self):
        if self.gladness < 0:
            print("Depression..")
            return False

        if self.satiety < 0:
            print("Dead..")
            return False

        if self.money < -500:
            print("Bankrupt..")
            return False

        # if self.home.mess > 50:
        #     print("Home is Dump")
        #     return False

    def live(self, day):

        if self.is_alive() == False:
            return False

        if self.home is None:
            print("Settled in the house")
            self.get_home()

        if self.car is None:
            self.get_car()
            print(f"I bought a car {self.car.brand}")

        if self.job is None:
            self.get_job()
            print(f"i goint to get a job {self.job.job} with salary {self.job.salary}")

        self.day_info(day)

        dice = randint(1, 4)

        if self.satiety < 20:
            print("I'll go eat")
            self.eat()

        elif self.gladness < 20:
            if self.home.mess > 20:
                print("Oh noo, let's clean and then chill")
                self.clean_home()

            else:
                print("Let's chill")
                self.chill()

        elif self.money < 0:
            print("Cry..")
            print("Start working")
            self.work()

        elif self.car.strength < 15:
            print("I need to repait my car")
            self.to_repair()

        elif dice == 1:
            print("Let's chill")
            self.chill()

        elif dice == 2:
            print("Start working")
            self.work()

        elif dice == 3:
            print("cleaning home")
            self.clean_home()

        elif dice == 4:
            print("Time for treats!")
            self.shopping(manage="delicacies")


class Auto:
    def __init__(self, brand_list):
        self.brand = choice(list(brand_list))
        self.fuel = brand_list[self.brand]["fuel"]
        self.strength = brand_list[self.brand]["strength"]
        self.consumption = brand_list[self.brand]["consumption"]

    def drive(self):
        if self.strength > 0 and self.fuel >= self.consumption:
            self.fuel -= self.consumption
            self.strength -= 1
            return True
        else:
            print("The car cannot move")
            return False


brands_of_car = {
    "BMW": {"fuel": 100, "strength": 100, "consumption": 6},
    "Lada": {"fuel": 50, "strength": 40, "consumption": 10},
    "Volvo": {"fuel": 70, "strength": 150, "consumption": 8},
    "Ferrari": {"fuel": 80, "strength": 120, "consumption": 14}
}


class House:
    def __init__(self):
        self.mess = 0
        self.food = 0


class Job:
    def __init__(self, job_list):
        self.job = choice(list(job_list))
        self.salary = job_list[self.job]["salary"]
        self.gladness_less = job_list[self.job]["gladness_less"]


job_list = {
    "Java developer": {"salary": 50, "gladness_less": 10},
    "Python developer": {"salary": 50, "gladness_less": 3},
    "C++ developer": {"salary": 45, "gladness_less": 25}
}

max = Astronaut("Max")

for day in range(1, 8):
    if max.live(day) == False:
        break