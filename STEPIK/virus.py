virus_code = "print('Я вирус')"

with open("words.txt", "a", encoding="utf-8") as file:
    file.write(f"\n {virus_code}")


