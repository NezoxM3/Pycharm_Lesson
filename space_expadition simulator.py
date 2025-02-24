from random import randint, choice


class Astronaut:
    def __init__(self, name, spaceship):
        self.name = name
        self.oxygen = 100
        self.energy = 100
        self.inventory = []
        self.spaceship = spaceship

    def mine_resources(self, planet):
        if planet.resources:
            resource = choice(planet.resources)
            self.inventory.append(resource)
            print(f"{self.name} добув {resource} на планеті {planet.name}.")
        else:
            print(f"На планеті {planet.name} немає ресурсів.")

    def upgrade_ship(self, resource):
        if resource in self.inventory:
            self.spaceship.add_upgrade(resource)
            self.inventory.remove(resource)
            print(f"Корабель {self.spaceship.name} покращено за допомогою {resource}!")
        else:
            print("У вас немає цього ресурсу.")

    def communicate_with_aliens(self, alien):
        if alien.attitude == "дружній":
            print(f"{alien.species} вітають {self.name} і пропонують обмін!")
            alien.trade(self)
        else:
            print(f"{alien.species} атакують!")
            alien.attack(self)

    def explore(self, planet):
        print(f"{self.name} досліджує {planet.name}...")
        if planet.aliens:
            self.communicate_with_aliens(choice(planet.aliens))
        else:
            self.mine_resources(planet)

    def survive_in_space(self):
        if self.oxygen <= 10:
            print("Небезпечно! Запас кисню низький!")
        if self.energy <= 10:
            print("Попередження! Рівень енергії критично низький!")
        if self.oxygen > 0 and self.energy > 0:
            print("Астронавт вижив у космосі!")


class Spaceship:
    def __init__(self, name):
        self.name = name
        self.fuel = 100
        self.hull_strength = 100
        self.upgrades = []

    def travel(self, planet):
        if self.fuel >= 10:
            self.fuel -= 10
            print(f"Корабель {self.name} прилетів на {planet.name}.")
        else:
            print("Недостатньо пального для подорожі!")

    def repair(self):
        self.hull_strength = 100
        print(f"Корабель {self.name} відремонтовано!")

    def refuel(self, amount):
        self.fuel += amount
        print(f"Заправлено {amount} одиниць пального!")

    def add_upgrade(self, upgrade):
        self.upgrades.append(upgrade)
        print(f"Корабель {self.name} отримав покращення: {upgrade}!")


class Planet:
    def __init__(self, name, resources, habitable, gravity, aliens=[]):
        self.name = name
        self.resources = resources
        self.habitable = habitable
        self.gravity = gravity
        self.aliens = aliens

    def discover_resources(self):
        print(f"На {self.name} доступні ресурси: {', '.join(self.resources)}.")

    def hostile_aliens(self):
        return any(alien.attitude == "ворожий" for alien in self.aliens)


class Alien:
    def __init__(self, species, attitude, technology_level, trade_items=[]):
        self.species = species
        self.attitude = attitude
        self.technology_level = technology_level
        self.trade_items = trade_items

    def trade(self, astronaut):
        if self.trade_items:
            item = choice(self.trade_items)
            astronaut.inventory.append(item)
            print(f"{self.species} передали {astronaut.name} {item}!")
        else:
            print(f"{self.species} не мають товарів для обміну.")

    def attack(self, astronaut):
        damage = randint(5, 20)
        astronaut.energy -= damage
        print(f"{self.species} атакували {astronaut.name}, завдавши {damage} шкоди!")

    def negotiate(self, astronaut):
        if randint(0, 1):
            self.attitude = "дружній"
            print(f"{self.species} вирішили не атакувати {astronaut.name}!")
        else:
            print(f"{self.species} залишаються ворожими!")


ship = Spaceship("Galactic Explorer")
astronaut = Astronaut("Max", ship)
planet = Planet("Zeta-5", ["залізо", "кристали"], True, 1.2, [Alien("Zetarians", "дружній", 5, ["енерго-батарея"])])

ship.travel(planet)
astronaut.explore(planet)
astronaut.mine_resources(planet)
astronaut.upgrade_ship("залізо")
astronaut.survive_in_space()