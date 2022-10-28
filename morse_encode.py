from random import randint


MORSE_ALPHABET = {"0": "-----", "1": ".----", "2": "..---", "3": "...--",
                "4": "....-", "5": ".....", "6": "-....", "7": "--...",
                "8": "---..", "9": "----.", "a": ".-", "b": "-...",
                "c": "-.-.", "d": "-..", "e": ".", "f": "..-.",
                "g": "--.", "h": "....", "i": "..", "j": ".---",
                "k": "-.-", "l": ".-..", "m": "--", "n": "-.",
                "o": "---", "p": ".--.", "q": "--.-", "r": ".-.",
                "s": "...", "t": "-", "u": "..-", "v": "...-",
                "w": ".--", "x": "-..-", "y": "-.--", "z": "--..",
                ".": ".-.-.-", ",": "--..--", "?": "..--..", "!": "-.-.--",
                "-": "-....-", "/": "-..-.", "@": ".--.-.", "(": "-.--.",
                 ")": "-.--.-"
                }

words_list = ["apple", "worm", "joke", "sun",
              "tree", "snow", "face", "zoo",
              "house", "farm", "hair", "lamp",
              "book", "wall", "table", "hand",
              "door", "window", "t-short", "eye"]

answers = []


def morse_encode(word: str) -> str:
    morse_word = ''
    for letter in word:
        if letter in MORSE_ALPHABET:
            morse_word += MORSE_ALPHABET[letter] + ' '
    return morse_word


def get_word(words_list: list) -> str:
    return words_list[randint(0, 19)]


def print_statistics(answers):
    correct_answers = answers.count(True)
    incorrect_answers = answers.count(False)
    print(f"Всего задачек: {len(answers)}")
    print(f"Отвечено верно: {correct_answers}")
    print(f"Отвечено неверно: {incorrect_answers}")
    


print("Сегодня мы потренируемся расшифровывать азбуку Морзе")
user_greetings = input("Нажмите Enter и начнем")

for answer in range(5):
    word = get_word(words_list)
    encode_word = morse_encode(word)
    print(encode_word)
    answer = input()
    if answer == word:
        print(f"Верно, {word}!")
        answers.append(True)
    else:
        print(f"Неверно, {word}!")
        answers.append(False)

print_statistics(answers)