# Sprawozdanie do zestawu zaliczeniowego AAP

## Zakres pracy

Sprawozdanie dotyczy zadań wykonanych w notebooku `AAP_Zestaw_Zaliczeniowy.ipynb`, ze szczególnym uwzględnieniem części implementacyjnych 1.1-6.1. Celem było nie tylko uzyskanie działającego kodu, ale też zachowanie zgodności z wymaganiami oraz sprawdzenie, czy rozwiązania są uruchamialne w lokalnym środowisku.

## Krótkie omówienie zadań

### Zadanie 1.1 - dekoratory `@retry` i `@cache_to_disk`

W tym zadaniu przygotowano dwa dekoratory: jeden odpowiada za ponawianie operacji po błędzie z użyciem exponential backoff, a drugi za zapisywanie wyników do cache na dysku. To połączenie dobrze pokazuje, jak można zwiększyć odporność kodu na błędy chwilowe i jednocześnie ograniczyć liczbę niepotrzebnych wywołań tej samej operacji. Najważniejszy wniosek praktyczny jest taki, że dekoratory są użyteczne nie tylko do "upiększania" składni, ale przede wszystkim do wydzielania powtarzalnych mechanizmów technicznych, takich jak retry i cache, poza główną logikę biznesową.

### Zadanie 2.1 - multiprocessing dla CPU-bound

Drugie zadanie dotyczyło zastosowania multiprocessing do pracy obciążającej procesor. Jego sens polega na pokazaniu różnicy między współbieżnością i realną równoległością: dla zadań CPU-bound same wątki w Pythonie zwykle nie dają oczekiwanego przyspieszenia z powodu GIL, natomiast osobne procesy już tak. Najważniejsza refleksja z tego ćwiczenia jest taka, że wybór modelu wykonania powinien wynikać z charakteru problemu, bo narzędzie dobre dla I/O-bound może być słabym wyborem dla obliczeń.

### Zadanie 3.1 - testowanie `Tokenizer` w pytest

W tej części przygotowano testy dla komponentu `Tokenizer` z użyciem `pytest`, fixtures i `parametrize`. Najważniejszy wniosek z tego zadania jest taki, że dobre testy powinny być możliwie małe, czytelne i niezależne od kolejności uruchamiania komórek. Dlatego rozwiązanie zostało doprowadzone do stanu, w którym można je uruchomić bez ukrytych zależności od wcześniejszego kontekstu notebooka.

### Zadanie 4.1 - SQLite w stylu NoSQL

Rozwiązanie wykorzystuje SQLite z kolumną JSON i pokazuje podejście schema-on-read, czyli interpretowanie struktury danych dopiero na etapie zapytania. To rozwiązanie jest wygodne przy danych półustrukturyzowanych, bo pozwala szybko iterować po modelu danych, ale kosztem gorszej przejrzystości i zwykle słabszej wydajności niż klasyczny model relacyjny. Zestawienie z wariantem tabelarycznym dobrze pokazuje, że elastyczność JSON jest cenna głównie wtedy, gdy struktura danych faktycznie często się zmienia.

### Zadanie 5.1 - analityka okienkowa w PySpark

W tej części użyto window functions do policzenia rankingu recenzji w obrębie klasy, top 3 najdłuższych recenzji, różnicy od średniej klasowej oraz moving average dla okna 50 obserwacji. Najważniejsza obserwacja praktyczna jest taka, że `groupBy` nie wystarcza do analizy pozycji rekordu w kontekście innych rekordów, a funkcje okienkowe pozwalają to zrobić bez utraty poziomu szczegółowości danych. Dodatkowo zadanie pokazało, że na Windows stabilność PySparka zależy od poprawnej konfiguracji `JAVA_HOME`, więc środowisko uruchomieniowe ma tu realny wpływ na powodzenie rozwiązania.

### Zadanie 6.1 - kontrakt danych i raport JSON

Ostatnie zadanie polegało na zbudowaniu prostego kontraktu danych z rozróżnieniem na reguły krytyczne (`error`) i ostrzeżenia (`warning`). Takie podejście ma sens, bo nie każda nieprawidłowość powinna zatrzymywać pipeline, ale część z nich musi blokować dalsze przetwarzanie, żeby nie propagować błędnych danych. Zapis raportu do pliku JSON jest przydatny operacyjnie, ponieważ daje artefakt możliwy do późniejszego audytu, integracji z monitoringiem albo porównywania wyników między uruchomieniami.

## Wnioski końcowe

Najważniejszy wspólny wniosek z tych zadań jest taki, że poprawne rozwiązanie to nie tylko implementacja logiki, ale również kontrola uruchamialności, zależności środowiskowych i jakości danych wejściowych. Zadania 3.1-6.1 dobrze pokazują pełny przekrój pracy inżynierskiej: od testowania, przez modelowanie danych i analitykę, aż po walidację jakości. W praktyce największą wartość daje połączenie tych elementów, bo dopiero wtedy rozwiązanie jest jednocześnie poprawne, sprawdzalne i użyteczne.