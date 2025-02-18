class Human:

    def __init__(self,name):
        self.name = name

class Auto:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
        self.passengers = []

    def add_passenger(self,*args):
        for passenger in args:
            self.passengers.append(passenger)


        def print_passenger_name(self):
            if self.passengers != []:
                print(f"Names of {self.brand} {self.model} passenger")

                for passenger in self.passengers:
                    print(passenger.name)

            else:
                print(f"There are no passengers in {self.brand} {self.model}")


nazar = Human("Nazar")
sasha = Human("Sasha")
andriy = Human("Andriy")
maks = Human("Maks")

car.add_passenger(nazar)
car.add_passenger(sasha)
car.add_passenger(andriy)
car.add_passenger(maks)


car.print_passenger_name()