#3. Словники (15 хв)
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
        print("4.Видалити контакт")
        print("5.Вийти")

        menu_choice = input("\nОберіть дію:")
        if menu_choice == "1":
            display_contacts()
        elif menu_choice == "2":
            add_contact()
        elif menu_choice == "3":
            search_contact()
        elif menu_choice == "4":
            delete_contact()
        elif menu_choice == "5":
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

def delete_contact():
    delete_user = input("Введіть ім'я контакту якого хочите видалити:")
    del phone_book[delete_user]
    print(f"Контакт {delete_user} успішно видалено.")

def search_contact():
    name2 = input("Введіть ім'я для пошуку: ")
    if name2 in phone_book:
        print(f"{name2}: {phone_book[name2]}")
    else:
        print(f"Контакт з ім'ям {name2} не знайдено.")

menu()