phone_book = {
    "Стас":"+380981678435",
    "Данік":"++380951873480",
    "Славік":"+380764696950",
}

def menu():
    while True:
        print("\nМеню")
        print("1.Показати всі контакти")
        print("2.Додати новий контакт")
        print("3.Знайти контакт")
        print("4.Вийти")

        menu_choice = input("\nОберіть дію:")
        if menu_choice == "1":
            display_contacts()
        elif menu_choice == "2":
            add_contact()
        elif menu_choice == "3":
            search_contact()
        elif menu_choice == "4":
            print("Закінчення роботи...")
            break
        else:
            print("Error, введітб один з нище перечислиних варіантів \n")


def display_contacts():
        print("\nКонтакти:")
        for name, phone_number in phone_book.items():
            print(f"{name}: {phone_number}")


def add_contact():
    name1 = input("Введіть ім'я нового контакту: ")
    phone_number1 = input("Введіть номер телефону: ")
    phone_book[name1] = phone_number1
    print(f"Контакт {name1} {phone_number1} успішно додано.")


def search_contact():
    name2 = input("Введіть ім'я для пошуку: ")
    if name2 in phone_book:
        print(f"{name2}: {phone_book[name2]}")
    else:
        print(f"Контакт з ім'ям {name2} не знайдено.")

menu()






grades = {
    "math":70,
    "python":850,
    "html&css":65,
    "sql":20,
    "English":90
}

avarage_grades = sum(grades.values()) / len(grades)

print("Student grades")

for subject, grade in grades.items():
    print(f"Subject: {subject} - {grade}")

print(f" Avarage student grade {avarage_grades:.0f}")






store_inventory = {
    "apple":5,
    "banana":3,
    "peach":12,
    "milk":20,
    "bread":12,
    "butter":20
}

product = input("Enter the produt, you would like to buy - ").lower()


if product in store_inventory:
    print(f"{product} is available at the store, it's price is {store_inventory[product]} coins.")

else:
    print("Sorry, product is unavailable")