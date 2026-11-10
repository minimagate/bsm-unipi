---
title: Algoritmo di eliminazione di Gauss
type: voce
categoria: metodo
corsi:
- Geometria 1
introdotta_in: 2026-10-22 - Sistemi lineari e algoritmo di eliminazione di Gauss
alias:
- Gauss
- eliminazione di Gauss
- eliminazione gaussiana
- riduzione di Gauss
- metodo di Gauss
sintesi: Procedimento che trasforma qualunque matrice in una matrice a scala usando solo operazioni elementari di riga.
---

L'**algoritmo di eliminazione di Gauss** trasforma una matrice qualsiasi in una matrice a scala usando solo operazioni elementari di riga. È il metodo standard per risolvere sistemi lineari e per calcolare rango, basi e intersezioni di sottospazi.

## Definizione

Data una matrice, si procede ricorsivamente:

1. si cerca la prima colonna non nulla della sottomatrice corrente;
2. con uno scambio di righe si porta un elemento non nullo in prima posizione: è il pivot;
3. per ogni riga sotto il pivot si fa $R_i\leftarrow R_i-\frac{a_{i1}}{a_{11}}R_1$, annullando la colonna sotto il pivot;
4. si ripete sulla sottomatrice a destra e in basso.

Alla fine si ottiene una matrice a scala.

## Intuizione

È l'eliminazione delle incognite "a cascata" che si fa a mano. Le operazioni di riga non cambiano le soluzioni, quindi il sistema a scala è equivalente a quello di partenza ma si risolve a ritroso, dall'ultima equazione verso l'alto. Le colonne senza pivot sono le variabili libere.

## Esempi

Per $\left(\begin{array}{cccc|c}1&1&-1&2&2\\0&0&1&1&-1\end{array}\right)$, già a scala, i pivot sono nelle colonne 1 e 3; ponendo $x_2=s$, $x_4=t$ si ottiene $x_3=-1-t$ e $x_1=1-s-3t$.

Per decidere se i vettori $v_1,\dots,v_k$ sono indipendenti si riduce la matrice con i vettori come colonne: lo sono se e solo se ogni colonna ha un pivot.

## Come si dimostra

Che l'algoritmo termini e produca una matrice a scala segue dalla struttura ricorsiva; che le soluzioni restino invariate segue dall'invertibilità delle operazioni. Si veda [[2026-10-22 - Sistemi lineari e algoritmo di eliminazione di Gauss#7. Algoritmo di eliminazione di Gauss|la lezione del 22 ottobre]].

## Vedi anche

- [[Matrice a scala]]
- [[Operazione elementare di riga]]
- [[Sistema lineare]]
- [[Forma ridotta a scala]]
- [[Rango]]
