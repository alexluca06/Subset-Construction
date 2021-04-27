336 CB LUCA AUREL-ALEXANDRU

	

	- Observatii:

	1.Atat tranzitiile din NFA, cat si cele din DFA sunt reprezentate prin intermediul
unui dictionar ce are ca chei un tuplu format din starea curenta si un caracter
(stare, caracter), iar ca valori o lista de stari urmatoare.

	2.Corespondenta dintre starile DFA-ului si starile din NFA este reprezentata
printr-un dictionar ce are ca chei starile DFA-ului, iar ca valoare o lista de
stari din NFA.


	-Explicatie functionalitati:

	Functia "epsilon_closure()" primeste ca parametrii o stare si tranzitiile
NFA-ului si intoarce o lista de stari ce reprezinta inchiderea pe epsilon a
starii primite ca parametru.

	Functia "extract_alphabet()" primeste ca parametru tranzitiile din NFA si
returneaza alfabetul folosit. Se parcurge lista de chei(list_keys): (stare, caracter)
si se extrag caracterele prezente.

	Functia "extract_final_state()" primeste ca parametrii starile finale din
NFA si un dictionar ce reprezinta o corespondenta intre starile DFA-ului si starile
NFA-ului, iar ca valoare de retur este lista de stari finale din DFA. Verifica in
dictionarul de corespondenta ce stari ale DFA-ului au ca corespondent o stare
ce este finala in NFA.

	Functia "write_file()" primeste ca parametrii numarul de stari din DFA,
lista de stari finale si dictionarul cu tranzitiile corespunzatoare. Aceasta
realizeaza scrierea rezultatului intr-un fisier primit ca argument in linia de
comanda.

	Functia "transform_in_dfa()" primeste ca parametrii starile finale din NFA,
dictionarul cu tranzitiile si alfabetul folosit de NFA, aceasta realizand
transformarea NFA-ului intr-un DFA.
Se pleaca cu starea initiala = 0 in DFA si i se asociaza in dictionarul de
corespondenta(correspondences) tot starea 0 din NFA, mai exact, inchiderea acesteia
pe epsilon. De asemenea, se creeaza si o lista(list_states) unde se salveaza starile
DFA-ului, initial, aceasta lista continand starea initiala = 0.
Functia parcurge aceasta lista cu stari din DFA(list_states), iar pentru fiecare
stare se extrage din dictionar lista de stari ce ii corespund in NFA(nfa_states).
Aceasta noua lista este, la randul ei, parcursa, iar pentru fiecare stare din lista si
caracter din alfabet se salveaza starile in care se ajunge in NFA care se adauga in
intr-o noua lista alaturi de inchiderile pe epsilon a starilor respective(new_states).
Lista(new_states) ce este sortata pentru a evita confuzia intre listele cu aceleasi
elemente, dar in ordine diferita(ele reprezinta aceeasi stare: [0, 1, 2] == [2,0,1]
cand vine vorba de stari).
Aceasta noua lista reprezinta starea urmatoare din DFA(va fi asociata cheie in
dictionarul de corespondenta ce reprezinta noua starea DFA). Apoi se verifica daca aceasta
noua stare se afla in dictionarul de corespondente, daca da, este adaugata tranzitia
in dictionarul de reprezentare a tranzitiilor DFA-ului(dfa), iar daca nu se gaseste,
aceasta este adaugata in dictionar cu o noua stare in DFA, se adauga noua stare in
lista de stari(list_states), dar si tranzitia in dictionarul de tranzitii(dfa).
Aceaste operatiuni se repeta pana se ajunge la finalul listei de stari(list_states),
deoarece sunt luate in calcul doar starile noi aparute care nu au tranzitii.
La final, se extrag starile finale a DFA-ului si rezultatul(nr de stari, starile finale si
tranzitiile sunt scrise intr-un fisier de iesire primit ca parametru in linia de comanda.

	In functia main este realizata citirea NFA-ului din fisier, extragerea alfabetului
si apelarea functiei de transformare a NFA-ului in DFA.

                                                              