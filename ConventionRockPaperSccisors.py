import random
def rock_paper_scissors():
    print('Welcome to the rock paper scissors game')

you = 0
computer = 0

while True:
    print('choose: 1-rock 2-paper 3-scissors')
    user_choice = input('your choice:')
    if user_choice not in ['1', '2', '3']:
        print('invalid choice try again')
        computer_choice = random.choice(['1', '2', '3'])
        continue
    computer_choice = random.choice(['1', '2', '3'])
    print('computer:', computer_choice)
    if user_choice == computer_choice:
        print('draw')
    elif (user_choice == '1' and computer_choice == '3') or (user_choice == '2' and computer_choice == '1') or (
            user_choice == '3' and computer_choice == '2'):
        print('you win')
        you += 1
    else:
        print('you lose')
        computer += 1
        print('score: you:', you, 'computer:', computer)
        print('play again? yes/no')
        again = input()
        if again == 'yes':
            continue
        else:
            print(f"final score: you:{you}comp:,{computer}")
            print('bye!')
        break

#Запуск функції
rock_paper_scissors()

