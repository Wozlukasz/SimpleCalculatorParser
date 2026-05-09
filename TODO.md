# Jesteś wolnym człowiekiem, więc zrobisz co zechcesz, ale to są moje porady i sugestie:

1. Aktualnie cała struktura parsowania składa się z obiektów klas "Node". Powinien być zawsze jeden główny korzeń i w nim są kolejne. Na podstawie danej klasy Node możesz określać co to ma być za działanie itd.

2. Myślałem, by interpreter z grubsza działał w kilku trybach/opcjach:
    - jeśli jest "=" i po obu stronach są wyrażenia bez zmiennych sprawdza czy Lewa = Prawa i zwraca T/F
    - jeśli nie ma "=" to po prostu liczy wynik
    - do tego obsługa przypisań (typu x = 34*7)
    - a ponadto definicja funkcji i późniejsze wywoływanie

Parsowanie zezwala na jeden znak = w danej linii i każde działanie musi być jawnie zapisane operatorem (nie ma mnożenia typu: 5(4-8), bo to za dużo wariantów wprowadza do obsługi...)

W kodzie dodałem komentarze CHYBA we wszystkich miejscach gdzie może wywalić błąd. To tam trzeba go jakoś obsłużyć i wypisać podpowiedź użytkownikowi co poszło nie tak.

Strukturę Lexera jeszcze przepiszę, bo się długa lista ifów zrobiła, ale funkcjonalnie pozostanie tak samo (chyba, że jakieś błędy znajdziemy to wiadomo...)