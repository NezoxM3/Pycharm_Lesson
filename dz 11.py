import random

choices = ["Камінь", "Ножиці", "Папір", "Ящірка", "Спок"]

player_score = 0
bot_score = 0

while True:
    print(f"Рахунок - Ти: {player_score} | Бот: {bot_score}")
    print("Виберіть варіант: Камінь, Ножиці, Папір, Ящірка, Спок")
    player_choice = input("Ваш вибір: ")

    if player_choice not in choices:
        print("Error. Виберіть: Камінь, Ножиці, Папір, Ящірка, Спок")
        continue

    bot_choice = random.choice(choices)
    print(f"Бот вибрав: {bot_choice}")

    if player_choice == bot_choice:
        print("Нічия!")
    elif player_choice == "Камінь":
        if bot_choice == "Ножиці":
            print("Ти виграв! Камінь > Ножиці.")
            player_score += 1
        elif bot_choice == "Ящірка":
            print("Ти виграв! Камінь > Ящірка.")
            player_score += 1
        else:
            print("Бот виграв! Камінь < Паперу і Споку.")
            bot_score += 1
    elif player_choice == "Ножиці":
        if bot_choice == "Папір":
            print("Ти виграв! Ножиці > Папір.")
            player_score += 1
        elif bot_choice == "Ящірка":
            print("Ти виграв! Ножиці > Ящірку.")
            player_score += 1
        else:
            print("Бот виграв! Ножиці < Каменю і Споку.")
            bot_score += 1
    elif player_choice == "Папір":
        if bot_choice == "Камінь":
            print("Ти виграв! Папір > Камінь.")
            player_score += 1
        elif bot_choice == "Спок":
            print("Ти виграв! Папір > Спок.")
            player_score += 1
        else:
            print("Бот виграв! Папір < Ножицям і Ящірці.")
            bot_score += 1
    elif player_choice == "Ящірка":
        if bot_choice == "Папір":
            print("Ти виграв! Ящірка > Папір.")
            player_score += 1
        elif bot_choice == "Спок":
            print("Ти виграв! Ящірка > Спок.")
            player_score += 1
        else:
            print("Бот виграв! Ящірка < Каменю і Ножицям.")
            bot_score += 1
    elif player_choice == "Спок":
        if bot_choice == "Ножиці":
            print("Ти виграв! Спок > Ножиці.")
            player_score += 1
        elif bot_choice == "Камінь":
            print("Ти виграв! Спок > Камінь.")
            player_score += 1
        else:
            print("Бот виграв! Спок < Паперу і Ящірці.")
            bot_score += 1

    if player_score == 5:
        print("Ти виграв гру з рахунком 5!")
        povtor = input("Хочете зіграти ще раз? (Да/Ні): ").lower()
        if povtor == "да":
            continue
        elif povtor == "ні":
            print("До побачення!")
            break
    elif bot_score == 5:
        print("Бот виграв гру з рахунком 5!")
        povtor = input("Хочете зіграти ще раз? (Да/Ні): ").lower()
        if povtor == "да":
            continue
        elif povtor == "ні":
            print("До побачення!")
            break
        else:
            print("Error")
            break

