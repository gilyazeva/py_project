from pin import check_pin

print("Введите ваш ПИН-код")

user_input = input()

if check_pin(user_input) is True:
    print("Такой ПИН-код подходит")
elif check_pin(user_input) is False:
    print("Такой ПИН-код НЕ подходит")









