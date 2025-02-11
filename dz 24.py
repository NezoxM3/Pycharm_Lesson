order_list = {}

while True:
    print("\n1.Переглянути все замовлення")
    print("2.Вибрати страву до замовлення")
    print("3.Закінчити і очікування замовлення")


    menu_choice = input("\nОберіть дію:")
    if menu_choice == "1":
        print("\nЗамовлення:")
        for dish, price in order_list.items():
            print(f"{dish}: {price}")
    elif menu_choice == "2":
        dish = input("Введіть страву яку хочите замовити: ")
        price = input("Її ціна: ")
        order_list[dish] = price
        print(f"До замовлення додано {dish} - {price}$.")
    elif menu_choice == "3":
        print("Дякую, що обрали наш ресторан, все ваше замовлення:")
        for dish, price in order_list.items():
            print(f"{dish}: {price}")
        break
    else:
        print("Не говоріть нісенітницю, що ви хочите зробити")

