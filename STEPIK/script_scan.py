print("Введите ваше имя")
user_name = input()

# счетчик очков
scores = 0
# всего сыграно игр
total_games = 0

import random

# открытие и чтение файла с английскими словами
with open("words.txt", "r") as file:
    for words in file:
        word = words.rstrip("\n")
        word_list = list(word)
        print(word_list)
        random.shuffle(word_list)
        word_shuffle = "".join(word_list)
        print(word_shuffle)
        print(f"Угадайте слово: {word_shuffle}")
        user_answer = input()
        print(word)
        print(user_answer)
        if user_answer == word:
            print("Верно! Вы получаете 10 очков.")
            scores += 10
        else:
            print(f"Неверно! Верный ответ – {word}.")

# открытие и редактирование файла с историей игр
with open("history.txt", "a") as file_history:
    file_history.write(f"{user_name} {scores}")


# открытие и чтение файла с историей игр
with open("history.txt", "r") as file_history:
    for line in file_history:
        total_games += 1

print(f"Всего игр сыграно: {total_games}")

