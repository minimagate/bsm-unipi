---
title: Rango
type: voce
categoria: definizione
corsi:
- Geometria 1
introdotta_in: 2026-10-23 - Sistemi lineari, nucleo, immagine e rango
alias:
- rango di una matrice
- rango per righe
- rango per colonne
sintesi: Dimensione dello spazio generato dalle colonne di una matrice, che coincide con quella dello spazio generato dalle righe.
---

Il **rango** di una matrice è la dimensione dello spazio generato dalle sue colonne. Dice quante colonne (o quante righe) sono davvero indipendenti.

## Definizione

Se $A\in M_{m,n}(\mathbb K)$ ha colonne $A_1,\dots,A_n$,

$$
\operatorname{rank}(A)=\dim\operatorname{span}\{A_1,\dots,A_n\}=\dim\operatorname{Im}(F_A),
$$

dove $F_A(x)=Ax$. Il rango per righe è la dimensione dello spazio generato dalle righe; i due numeri coincidono, quindi $\operatorname{rank}(A)=\operatorname{rank}(A^T)\leq\min\{m,n\}$.

## Intuizione

Il rango è la "dimensione effettiva" dell'immagine della mappa $x\mapsto Ax$. Si calcola con Gauss: le operazioni di riga non lo cambiano, e per una matrice a scala è il numero di pivot (o di righe non nulle). Il rango controlla anche i sistemi lineari: $\dim\ker(F_A)=n-\operatorname{rank}(A)$.

## Esempi

La matrice $\begin{pmatrix}1&2\\2&4\end{pmatrix}$ ha rango $1$: la seconda colonna è il doppio della prima.

La matrice $\begin{pmatrix}1&0&1\\0&1&1\\0&0&0\end{pmatrix}$ è a scala con due pivot, quindi ha rango $2$.

## Come si dimostra

L'uguaglianza tra rango e dimensione dell'immagine segue da $Ax=x_1A_1+\cdots+x_nA_n$, come spiegato [[2026-10-23 - Sistemi lineari, nucleo, immagine e rango#Rango di una matrice|nella lezione del 23 ottobre]]. L'invarianza per Gauss e l'uguaglianza tra rango per righe e per colonne sono dimostrate [[2026-10-27 - Rango, sistemi lineari e matrici elementari#8. Rango per righe e rango per colonne|il 27 ottobre]].

## Vedi anche

- [[Teorema rango-nullità]]
- [[Teorema di Rouché-Capelli]]
- [[Matrice a scala]]
- [[Applicazione lineare]]
