# Prosty parser wyrażeń matematycznych

## Autorzy:
- Julian Szamotuła
- Łukasz Woźniak


Prosty i rozszerzalny interpreter wyrażeń matematycznych napisany w Pythonie od podstaw. Projekt implementuje własny analizator leksykalny (Lexer), parser generujący drzewo składniowe (AST) oraz interpreter oparty na wzorcu projektowym *Visitor* (odwiedzający). 

Program działa w trybie REPL (Read-Eval-Print Loop), pozwalając na interaktywne wprowadzanie równań do konsoli.

## Możliwości

* **Podstawowa arytmetyka:** Dodawanie (`+`), odejmowanie (`-`), mnożenie (`*`), dzielenie (`/`), potęgowanie (`^`).
* **Kolejność działań:** Pełne wsparcie dla nawiasów `()` oraz matematycznej kolejności wykonywania operacji.
* **Zmienne:** Możliwość deklarowania własnych zmiennych i korzystania z nich w kolejnych linijkach.
* **Stałe matematyczne:** Wbudowane wsparcie dla `pi` oraz `e`.
* **Wbudowane funkcje:** Obsługa funkcji wieloargumentowych i jednoargumentowych, m.in.: `sin()`, `cos()`, `tan()`, `sqrt()`, `log()`, `max()`, `min()`, `abs()`.
* **Obsługa błędów:** Wykrywanie dzielenia przez zero, niepoprawnej składni (Syntax Error) czy niezdefiniowanych zmiennych.

## Uruchomienie

Aby uruchomić kalkulator, upewnij się, że masz zainstalowanego Pythona (wersja 3.x), a następnie uruchom główny plik w terminalu:

```bash
python main.py
```

Aby opuścić program, wpisz `exit` lub `quit`.

## Składnia i użycie

Po uruchomieniu skryptu pojawi się znak zachęty `> `, gdzie możesz wprowadzać swoje wyrażenia.

**Przykładowa sesja:**

```text
Kalkulator uruchomiony. Wpisz równanie lub 'exit' aby wyjść.
> 2 + 2 * (3 ^ 2)
20.0

> max(10, 20) + sin(pi)
20.0

> x = 5
Utworzono zmienną x = 5.0

> y = x * 3
Utworzono zmienną y = 15.0

> y / x
3.0

```

## Struktura projektu

Architektura projektu została podzielona na moduły odpowiadające poszczególnym etapom przetwarzania tekstu:

* `main.py` - Punkt wejścia aplikacji. Odpowiada za pętlę REPL, pobieranie wejścia od użytkownika i łączenie wszystkich komponentów.
* `calc_tokens.py` - Definiuje typy tokenów (np. liczby, operatory, nawiasy) za pomocą struktury `Enum` oraz klasę `Token`.
* `calc_lexer.py` - Analizator leksykalny. Czyta surowy tekst znak po znaku i zamienia go na ciąg zrozumiałych dla parsera tokenów, odrzucając białe znaki.
* `nodes.py` - Zestaw struktur danych (Data Classes) reprezentujących węzły Abstrakcyjnego Drzewa Składniowego (AST). Każda operacja (np. dodawanie, wywołanie funkcji) ma swój odpowiedni węzeł.
* `calc_parser.py` - Parser oparty na metodzie zejść rekurencyjnych (Recursive Descent Parser). Przetwarza listę tokenów i buduje z nich odpowiednio zagnieżdżone drzewo AST, pilnując poprawności składni.
* `calc_interpreter.py` - Właściwy interpreter wykorzystujący wzorzec *Visitor*. Odwiedza poszczególne węzły drzewa AST od dołu do góry i oblicza ich ostateczną wartość liczbową, operując również na zmiennych i funkcjach wbudowanych.


