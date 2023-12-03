import difflib
import random
from words1000 import words_dict

def is_similar(a, b):
    similarity = difflib.SequenceMatcher(None, a, b).ratio()
    return similarity > 0.8

def english_training():
    print("Let's practice! Write the translation into English or Russian for the following word:")
    while True:
        lang = random.choice(["english", "russian"])

        if lang == "english":
            russian_word = random.choice(list(words_dict.keys()))
            correct_translation = words_dict[russian_word]

            english_translations = list(words_dict.values())
            english_translations.remove(correct_translation)


            translations = [correct_translation] + random.sample(english_translations, 2)
            random.shuffle(translations)

            print(f"\nChoose the correct translation into English for this word:")
            print(f"✔️{russian_word}✔️")

            # Печатаем варианты ответов
            for i, translation in enumerate(translations, start=1):
                print(f"{i}. {translation}")

            user_choice = int(input("Enter the number of the correct translation (or '0' to exit): "))
            if user_choice == 0:
                break

            user_translation = translations[user_choice - 1]

            if user_translation == correct_translation:
                print("Correct!✅✅✅")
            elif is_similar(user_translation.lower(), correct_translation.lower()):
                print("Close!✅✅✅ Your answer is close to the correct one.")
                print(f"Correct answer✔️: {correct_translation}")
            else:
                print(f"Incorrect. Correct answer✔️: {correct_translation}")

        else:
            english_word = random.choice(list(words_dict.values()))
            correct_translation = list(words_dict.keys())[list(words_dict.values()).index(english_word)]

            russian_translations = list(words_dict.keys())
            russian_translations.remove(correct_translation)


            words = [correct_translation] + random.sample(russian_translations, 2)
            random.shuffle(words)

            print(f"\nChoose the correct translation into Russian for this word:")
            print(f"✔️{english_word}✔️")


            for i, word in enumerate(words, start=1):
                print(f"{i}. {word}")

            user_choice = int(input("Enter the number of the correct translation (or '0' to exit): "))
            if user_choice == 0:
                break

            user_word = words[user_choice - 1]

            if user_word.lower() == correct_translation.lower():
                print("Correct!✅✅✅")
            elif is_similar(user_word.lower(), correct_translation.lower()):
                print("Close!✅✅✅ Your answer is close to the correct one.")
                print(f"Correct answer: {correct_translation}✔️")
            else:
                print(f"Incorrect. Correct answer: {correct_translation}✔️")

if __name__ == "__main__":
    english_training()
