
**Program usuwa cykle z grafu. Algorytm Kruskala**
==============================================
<p>Program wykonany w języku Python.

Wejściowe dane
------------------
<p>Program wczytuje dane od użytkownika. 

Użytkownik musi podać ilość wierzchołków (N) grafu, ilość krawędzi (M) i potem podać połączenia wierzchołków wartośi krawędzi między nimi (from a to b with weight w).
 

Przykładowe dane:

    Please enter the number of vertices: 6
    Please enter the number of edge: 7
    
    Enter a b w -> meaning edge from a to b with weight w
    1 2 1
    1 6 4 
    3 5 3
    2 5 1
    2 4 2
    3 6 2
    1 3 2

Poprawne wyjściowe dane dla tego grafu:

    1 <-> 2 weight: 1
    2 <-> 5 weight: 1
    2 <-> 4 weight: 2
    3 <-> 6 weight: 2
    1 <-> 3 weight: 2

Jak uruchomić program
--------------------------

Z poziomu konsoli: 

