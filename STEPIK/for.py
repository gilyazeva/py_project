income = int(input())

necessity_jar = round(55 / 100 * income) # Текущие расходы
financial_freedom_jar = round(10 / 100 * income)  # Финансовая свобода
education_jar = round(10 / 100 * income)  # Образование
savings_jar = round(10 / 100 * income) # Резервный фонд
play_jar = round(10 / 100 * income) # Развлечения
give_jar = round(5 / 100 * income) # Благотворительность и подарки

print(f"Текущие расходы {necessity_jar}")
print(f"Финансовая свобода {financial_freedom_jar}")
print(f"Образование {education_jar}")
print(f"Резервный фонд {savings_jar}")
print(f"Развлечения {play_jar}")
print(f"Благотворительность и подарки {give_jar}")