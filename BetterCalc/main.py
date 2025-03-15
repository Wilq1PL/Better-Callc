version = "1.1 alpha"
def hello(ver):
    print(f"Better Calc by Wilq1PL\nVersion {ver}")
    choose_counting(selecting_menu())

def is_number(value):
    try:
        int(value)  # Sprawdzamy, czy da się przekonwertować na liczbę całkowitą
        return True
    except ValueError:
        return False

def selecting_menu():
    menu = ["Pole prostokąta", "Pole trójkąta", "Pole trapezu", "Pole koła"] #Lista dostępnych opcji

    def print_menu():
        print("\nWybierz opcję:")
        for idx, item in enumerate(menu, start=1):
            print(f"{idx}. {item}")

    while True:
        print_menu()
        selection = input("Wybieram: ").strip()

        if not is_number(selection):
            print("❌ Podano niepoprawną wartość. Proszę wpisać numer opcji.\n")
            continue  # Powtarzamy pętlę

        selection = int(selection)
        if 1 <= selection <= len(menu):  # Dynamiczna weryfikacja poprawnych opcji
            print(f"✅ Wybrano: {menu[selection - 1]}\n")
            return selection
        else:
            print("❌ Podano nieistniejący numer opcji. Spróbuj ponownie.\n")

def choose_counting(selection):
    if selection == 1:
        count_rectangle()
    elif selection == 2:
        count_triangle()

def count_rectangle():
    while True:
        x = int(input("Podaj wymiary pierwszego boku:"))

        if not is_number(x):
            print("❌ Podano niepoprawną wartość. Proszę wpisać liczbę.\n")
            continue  # Powtarzamy pętlę
        else:
            print(f"Podano: x = {x}\n")
            break
    while True:
        y = int(input("Podaj wymiary drugiego boku:"))

        if not is_number(y):
            print("❌ Podano niepoprawną wartość. Proszę wpisać liczbę.\n")
            continue  # Powtarzamy pętlę
        else:
            print(f"Podano: y = {y}\n")
            break
    print(f"Wynikiem działania jest:\n{x*y}")

def count_triangle():
    while True:
        x = int(input("Podaj wymiary podstawy:"))

        if not is_number(x):
            print("❌ Podano niepoprawną wartość. Proszę wpisać liczbę.\n")
            continue  # Powtarzamy pętlę
        else:
            print(f"Podano: x = {x}\n")
            break
    while True:
        h = int(input("Podaj wymiary wysokości:"))

        if not is_number(h):
            print("❌ Podano niepoprawną wartość. Proszę wpisać liczbę.\n")
            continue  # Powtarzamy pętlę
        else:
            print(f"Podano: h = {h}\n")
            break
    sum_xh = x * h
    print(f"Wynikiem działania jest:\n{sum_xh/2}")

if __name__ == "__main__":
    hello(version)
