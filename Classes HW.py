class ProgrammingLanguage:
    def __init__(self, name, typing, popularity, year):
        self.name = name
        self.typing = typing
        self.popularity = popularity
        self.year = year

    def is_popular(self):
        if self.popularity > 80:
            return f"{self.name} є дуже популярною мовою програмування!"
        elif self.popularity > 50:
            return f"{self.name} має середню популярність."
        else:
            return f"{self.name} не дуже популярна."

    def __str__(self):
        return f"Мова програмування: {self.name}, Тип: {self.typing}, Рік створення: {self.year}, Популярність: {self.popularity}%"


python = ProgrammingLanguage("Python", "Динамічно типізована", 95, 1991)
java = ProgrammingLanguage("Java", "Статично типізована", 85, 1995)
c = ProgrammingLanguage("C", "Статично типізована", 65, 1972)

print(python)
print(java)
print(c)

print(python.is_popular())
print(java.is_popular())
print(c.is_popular())