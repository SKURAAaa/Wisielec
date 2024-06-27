import random


def read_word_list(file_path):
    """
    Funkcja do wczytania listy haseł z pliku tekstowego.
    """
    with open(file_path, 'r') as file:
        word_list = file.readlines()
    return word_list


def save_score(nickname, points, file_path):
    """
    Funkcja do zapisania wyniku gry do pliku tekstowego.
    """
    with open(file_path, 'a') as file:
        file.write(f"{nickname};{points}\n")


def hangman_game(word):
    """
    Funkcja obsługująca grę w "wisielca".
    """
    # Inicjalizacja zmiennych
    guessed_letters = []
    lives = 7
    points = 100

    # Wyświetlenie pustych miejsc dla liter
    hidden_word = ['_' if letter.isalpha() else letter for letter in word]
    print(" ".join(hidden_word))

    # Pętla główna gry
    while '_' in hidden_word and lives > 0:
        # Wczytanie literki od gracza
        guess = input("Podaj literę: ").lower()

        # Sprawdzenie, czy litera została już podana
        if guess in guessed_letters:
            print("Ta litera została już podana. Spróbuj ponownie.")
            continue

        # Dodanie literki do listy użytych liter
        guessed_letters.append(guess)

        # Sprawdzenie, czy litera znajduje się w słowie
        if guess in word:
            print("Dobra odpowiedź!")
            for i in range(len(word)):
                if word[i] == guess:
                    hidden_word[i] = guess
        else:
            print("Błędna odpowiedź!")
            lives -= 1
            points -= 1

        # Wyświetlenie stanu gry
        print(" ".join(hidden_word))
        print(f"Życia: {lives}")

    # Zakończenie gry
    if '_' not in hidden_word:
        print("Gratulacje! Odgadłeś hasło!")
    else:
        print("Przegrałeś! Hasło to:", word)
        points -= 100

    print(f"Uzyskane punkty: {points}")
    return points


# Ścieżka do pliku z hasłami
file_path = "C:\\Users\\s25972\\PycharmProjects\\lab4_zad2\\text.txt"

# Wczytanie listy haseł
word_list = read_word_list(file_path)

# Losowanie hasła
chosen_word = random.choice(word_list).strip()

# Rozpoczęcie gry
nickname = input("Podaj swój pseudonim: ")
points = hangman_game(chosen_word)

# Zapisanie wyniku
save_score(nickname, points, "wyniki.txt")

