
**Program usuwa cykle z grafu. Algorytm Kruskala**
==============================================
<p>Program wykonany w jezyku Python.

Wejściowe dane
------------------
<p>Program wczytuje dane od uzytkownika. 

Użytkownik podaje nazwe pliku jako argument funkcji `KruskalAlgorithm()`, w przeciwnym wypadku graf zostanie wczytany z domyslnego pliku 'graph.txt'.
W pliku musi zostac podana lista sasiedztwa grafu w postaci:

`wierzcholek_a  wierzchowek_b waga_krawedzi`

Przykladowe dane dla graph.txt:

    1 2 1
    2 5 1
    2 4 2
    3 6 2
    1 3 2
    3 5 3
    1 6 4
    
Poprawne wyjsciowe dane dla grafu:

    1 - 2 weight: 1
    2 - 5 weight: 1
    2 - 4 weight: 2
    3 - 6 weight: 2
    1 - 3 weight: 2
    

Zadanie z https://pl.wikipedia.org/wiki/Algorytm_Kruskala

    1 3 1
    4 5 2
    1 2 3
    2 3 4
    2 4 5
    3 4 6
    3 5 7


Poprawne wyjsciowe dane dla grafu:

    1 - 3 weight: 1
    4 - 5 weight: 2
    1 - 2 weight: 3
    2 - 4 weight: 5

Jak uruchomić program
--------------------------

Z poziomu konsoli: 

`python kruskal_algorithm.py` dla Windows 

`python3 kruskal_algorithm.py` dla Linux / Mac OS 

Opis algorytmu
--------------------------
Algorytm Kruskala znajduje minimalne drzewo rozpinajace grafu.

Algorytm jest zachlanny, znaczy to ze podejmuje on najlepszy krok dla danej sytuacji i zestawu danych. 
Graf wczytany musi byc spojny, nieskierowany, wazony, czyli jego krawedzie musza miec wage. 


Opis programu
--------------------------
Program wczytuje graf z pliku graph.txt lub innego, podanego przez uzytkownika. 

Graf jest przechowywany jako lista krawedzi, gdzie krawedz to wartosci - `a, b, w` (wierzcholek_a  wierzchowek_b waga_krawedzi).
Dlugosc listy odpowiada ilosci krawedzi, a przy ladowaniu grafu wartosci `a, b` zostaja dodane do zbioru wierzcholkow, ktora potrzebujemy dla znalezienia ilosci wierzcholkow.

Nastepnie zaladowany graf zostaje posortowany wedlug wagi krawedzi, poniewaz drzewo rozpinajace musi skladac sie z najmniejszych wartosci wag.

Glowna metoda w algorytmie klasy `KruskalAlgorithm` - `run()` polega na sprawdzaniu cykli w grafie i wypelnianiu tablicy zaleznosci `parents`.
Jezeli wierzcholki nie maja wspolnych rodzicow to dodajemy je do drzewa rozpinajacego, a nastepnie 'laczymy' w tablicy `parents` za pomoca funkcji `join()`.
Metoda `run()` zwraca nam dzrewo rozpinajace.



