from validators.validate_pin import validate_pin
from validators.validate_card import validate_card

print("Введите ваш номер карты")
card_number = input()
print("Введите ваш ПИН-код")
card_pin = input()

if validate_card(card_number) is True:
    print("Номер карты допустимый")
elif validate_card(card_number) is False:
    print("Номер карты недопустимый")

if validate_pin(card_pin) is True:
    print("ПИН-код допустимый")
elif validate_pin(card_pin) is False:
    print("ПИН-код недопустимый")
