class Course:
    def __init__(self, name, instructor, duration):
        self.name = name
        self.instructor = instructor
        self.duration = duration

    def about_course(self):
        print(f"Курс: {self.name}, Викладач: {self.instructor}, Тривалість: {self.duration}")

    def is_long_course(self):
        return self.duration > 40


course1 = Course("Дизайн", "Ігор Карась", 35)
course2 = Course("Програмування", "Юра Малик", 40)
course3 = Course("Створенню програм на Arduino","Богдан Іванчук", 50)


course1.about_course()
print(course1.is_long_course())
course2.about_course()
print(course2.is_long_course())
course3.about_course()
print(course3.is_long_course())
