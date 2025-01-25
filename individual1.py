def calculate_percentage_of_a(sentence):
    total_letters = sum(1 for char in sentence if char.isalpha())  # Количество букв
    count_a = sentence.lower().count('а')  # Количество букв "а"

    return (count_a / total_letters) * 100 if total_letters > 0 else 0


# Ввод предложения с клавиатуры
sentence = input("Введите предложение: ")

result = calculate_percentage_of_a(sentence)
print(f"Доля букв 'а' в предложении: {result:.2f}%")
