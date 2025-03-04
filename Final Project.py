import random
import time


class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.hunger = 50
        self.thirst = 50
        self.food = 2
        self.water = 2
        self.days_survived = 0

    def eat(self):
        if self.food > 0:
            self.food -= 1
            self.hunger = min(100, self.hunger + 20)
            print(f"{self.name} поїв. Голод: {self.hunger}, Їжі залишилось: {self.food}")
        else:
            print("Їжа скінчилася")

    def drink(self):
        if self.water > 0:
            self.water -= 1
            self.thirst = min(100, self.thirst + 20)
            print(f"{self.name} випив води. Спрага: {self.thirst}, Води залишилось: {self.water}")
        else:
            print("Вода скінчилася")

    def rest(self):
        self.health = min(100, self.health + 10)
        self.days_survived += 1
        time.sleep(1.5)
        print(f"\nДень {self.days_survived}")
        print(f"{self.name} відпочив. Здоров'я: {self.health}")

        if self.days_survived % 2 == 0:
            self.hunger = max(0, self.hunger - 20)
            self.thirst = max(0, self.thirst - 20)

        if self.hunger == 0 or self.thirst == 0:
            self.health = max(0, self.health - 5)

        if self.health == 0:
            print(f"Гра закінчена. Ви прожили {self.days_survived} днів")
            exit()

    def explore(self, world):
        self.days_survived += 1
        print(f"\nДень {self.days_survived}")
        print(f"{self.name} вирушив на дослідження...")
        time.sleep(1.5)
        world.generate_event(self)

        if self.days_survived % 2 == 0:
            self.hunger = max(0, self.hunger - 20)
            self.thirst = max(0, self.thirst - 20)

        if self.hunger == 0 or self.thirst == 0:
            self.health = max(0, self.health - 5)

        if self.health == 0:
            print(f"Гра закінчена. Ви прожили {self.days_survived} днів.")
            exit()

    def status(self):
        print(
            f"\n{self.name} - Здоров'я: {self.health}, Голод: {self.hunger}, Спрага: {self.thirst}, Їжа: {self.food}, Вода: {self.water}, Дні виживання: {self.days_survived}\n")


class World:
    def generate_event(self, player):
        event_roll = random.randint(1, 5)

        if event_roll == 1:
            print("Подія: Знайдено джерело води!")
            player.water += 2
        elif event_roll == 2:
            print("Подія: Знайдено їжу!")
            player.food += 2
        elif event_roll == 3:
            print("Подія: Атака дикого звіра")
            player.health = max(0, player.health - 30)
        elif event_roll == 4:
            print("Подія: погана погода!")
            player.health = max(0, player.health - 10)
        else:
            print("Подія: Нічого сьогодні не знайдено.")

        if player.health == 0:
            print(f"Гра закінчена. Ви прожили {player.days_survived} днів.")
            print(f"Дякую, що пограли в гру, створеною Пислар Максимом")
            exit()


def main():
    name = input("Введіть ім'я гравця: ")
    player = Player(name)
    world = World()

    while True:
        player.status()
        action = input("Оберіть дію: (eat, drink, explore, rest, exit): ").strip().lower()

        if action == "eat":
            player.eat()
        elif action == "drink":
            player.drink()
        elif action == "explore":
            player.explore(world)
        elif action == "rest":
            player.rest()
        elif action == "exit":
            print(f"Гра завершена. Ви прожили {player.days_survived} днів.")
            print(f"Дякую, що пограли в гру, створеною Пислар Максимом")
            break
        else:
            print("Введіть одну з вищеперечислених дій")


main()