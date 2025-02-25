#Робота зі словниками (15 хв)
dict = {"hello": "Привіт",
        "chair": "стілець",
        "table": "стіл",
        "statue": "статуя",
        "boat": "корабель",
        "car": "машина",
        "plane": "літак",
        "picture": "фотографія",
        "frame": "рамка",
        "lightbulb": "лампочка",
        "box": "коробка",
        "door": "двері"
}

english_word = input("Введіть англійське слово: ").lower()
ukrainian_word = dict.get(english_word)

print(f"По українські це буде {ukrainian_word}")