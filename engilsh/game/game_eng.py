import difflib
import random
from words1000 import words_dict





def is_similar(a, b):
    similarity = difflib.SequenceMatcher(None, a, b).ratio()
    return similarity > 1



def english_training():
    print("Давайте потренируемся! Напишите перевод на русский или английский для следующего предложения:")
    while True:

        lang = random.choice(["english", "russian"])

        if lang == "english":
            sentence = random.choice(list(words_dict.keys()))
            correct_translation =words_dict[sentence]

            print(f"\nTranslate this phrase into Russian:")
            print(f"{sentence}")
            user_translation = input("Перевод на русский (или 'exit' для выхода): ").strip().lower()
        else:
            sentence = random.choice(list(words_dict.values()))
            correct_translation = list(words_dict.keys())[list(words_dict.values()).index(sentence)]

            print(f"\nTranslate this phrase into English:")
            print(f"{sentence}")
            user_translation = input("Перевод на английский (или 'exit' для выхода): ").strip().lower()

        if user_translation == 'exit':
            break

        if user_translation == correct_translation.lower():
            print("Правильно!✅✅✅")
        elif is_similar(user_translation, correct_translation.lower()):
            print("Почти правильно!✅✅✅ Ваш ответ близок к правильному.")
            print(f"Правильный ответ: {correct_translation}")
        else:
            print(f"Неправильно. Правильный ответ😳😳😳: {correct_translation}")


if __name__ == "__main__":
    english_training()