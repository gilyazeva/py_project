answers = ['False', 'False', 'False', 'True', 'True']

total_questions = len(answers)
correct_answers = 0
wrong_answers = 0

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

  return correct_answers
  return wrong_answers
  return total_questions



print_statistics(answers)


print(f"Всего задачек: {total_questions}")
print(f"Отвечено верно: {correct_answers}")
print(f"Отвечено неверно: {wrong_answers}")


