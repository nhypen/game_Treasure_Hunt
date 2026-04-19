import random

SIZE = 3
ATTEMPTS = 5

treasure_row = random.randint(0, SIZE - 1)
treasure_col = random.randint(0, SIZE - 1)

board = [["◻️" for _ in range(SIZE)] for _ in range(SIZE)]

def show_board():
    print("\nMapa:")
    print("   1 2 3")
    for i, row in enumerate(board, start=1):
        print(f"{i}  " + " ".join(row))
    print()

print("🏴‍☠️TREASURE HUNT 🏴‍☠️")
print("Znajdź skarb na mapie 3x3!")
print("Masz 5 prób.")
print("Legenda:")
print("◻️ = nieodkryte pole")
print("❌ = puste pole")
print("💎 = skarb\n")

for attempt in range(1, ATTEMPTS + 1):
    show_board()
    print(f"Próba {attempt}/{ATTEMPTS}")

    try:
        row = int(input("Podaj wiersz (1-3): ")) - 1
        col = int(input("Podaj kolumnę (1-3): ")) - 1
    except ValueError:
        print("❌ Wpisz liczbę.\n")
        continue

    if row < 0 or row >= SIZE or col < 0 or col >= SIZE:
        print("To pole jest poza mapą.\n")
        continue

    if board[row][col] == "❌":
        print("To pole już sprawdzałeś.\n")
        continue

    if row == treasure_row and col == treasure_col:
        board[row][col] = "💎"
        show_board()
        print("Znalazłeś skarb! Wygrałeś!")
        break
    else:
        board[row][col] = "❌"
        print("Tu nie ma skarbu.")

        if row < treasure_row:
            print(" Skarb jest niżej.")
        elif row > treasure_row:
            print("Skarb jest wyżej.")

        if col < treasure_col:
            print("Skarb jest bardziej w prawo.")
        elif col > treasure_col:
            print("Skarb jest bardziej w lewo.")

        print()

else:
    board[treasure_row][treasure_col] = "💎"
    show_board()
    print("Koniec prób")
    print("Koniec gry")
