print("Привет!")
print("Предлагаю проверить свои знания английского! ")
print("Расскажи, как тебя зовут! ")
user_name = input()
print(f"Привет, {user_name}, начинаем тренировку!")

right_answer = 0
number_of_points = 0
total_questions = 3

question_1 = input("My name ___ Vova ")
if question_1 == "is":
    print("Ответ верный!")
    print("Вы получаете 10 баллов!")
    right_answer += 1
    number_of_points += 10
else:
    print("Неправильно.")
    print("Правильный ответ: is")

question_2 = input("I ___ a coder ")
if question_2 == "am":
    print("Ответ верный!")
    print("Вы получаете 10 баллов!")
    right_answer += 1
    number_of_points += 10
else:
    print("Неправильно.")
    print("Правильный ответ: am")

question_3 = input("I live ___ Moscow ")
if question_3 == "in":
    print("Ответ верный!")
    print("Вы получаете 10 баллов!")
    right_answer += 1
    number_of_points += 10
else:
    print("Неправильно.")
    print("Правильный ответ: in")

percentage_of_correct_answers = round(right_answer / total_questions * 100)

print(f"Вот и всё, {user_name}")
print(f"Вы ответили на {right_answer} вопросов из 3 верно")
print(f"Вы заработали {number_of_points} баллов")
print(f"Это {percentage_of_correct_answers} процентов")
