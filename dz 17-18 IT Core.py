def test_results():
    print("Test Results System")

#Даємо змінним значення 0
    total_students = 0
    passed_students = 0
    failed_students = 0

#Поки не закінчим програму
    while True:
        result = input("Enter 'pass' for passed, 'fail' for failed, or 'end' to stop: ")

        if result == "end":
            break

        if result == "pass":
            passed_students += 1
            total_students += 1
        elif result == "fail":
            failed_students += 1
            total_students += 1
        else:
            print("Invalid input, try again!")

#Підраховуємо процент успішних студентів
    pass_percentage = (passed_students / total_students * 100) if total_students > 0 else 0

#Перевіряємо кінцевий результат
    print("\nResults Summary")
    print("Total Students:", total_students)
    print("Passed Students:", passed_students)
    print("Failed Students:", failed_students)
    print("Pass Percentage:", pass_percentage)

#Запускаємо функцію
test_results()
