answers = ['False', 'False', 'True', 'True', 'True']


def print_statistics(answers):
  correct_answers = 0
  wrong_answers = 0
  total_questions = 0

  for i in answers:
    total_questions += 1
    if i == "True":
      correct_answers += 1
    elif i == "False":
      wrong_answers += 1

  print(f"Всего задачек: {total_questions}")
  print(f"Отвечено верно: {correct_answers}")
  print(f"Отвечено неверно: {wrong_answers}")



print_statistics(answers)


