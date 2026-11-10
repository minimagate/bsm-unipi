---
title: Forma ridotta a scala
type: voce
categoria: definizione
corsi:
- Geometria 1
introdotta_in: 2026-10-27 - Rango, sistemi lineari e matrici elementari
alias:
- forma completamente ridotta a scala
- matrice ridotta a scala
sintesi: Matrice a scala in cui ogni pivot vale uno ed è l'unico elemento non nullo della propria colonna.
---

Una matrice è in **forma ridotta a scala** (o completamente ridotta) quando è a scala e, in più, i pivot sono tutti uguali a $1$ e sopra e sotto ciascun pivot ci sono solo zeri. È la versione "ripulita" della forma a scala.

## Definizione

Una matrice è completamente ridotta a scala se:

- ogni pivot è uguale a $1$;
- nella colonna di ogni pivot tutti gli altri elementi sono nulli;
- i pivot avanzano verso destra scendendo di riga;
- le righe nulle sono in fondo.

Si ottiene da una matrice a scala in due passi: si divide ogni riga per il suo pivot e poi si usano operazioni elementari per annullare gli elementi sopra i pivot.

## Intuizione

Da questa forma si leggono subito rango (numero di pivot), variabili pivot e libere, e le soluzioni di un sistema. È anche una forma canonica: ogni matrice è equivalente a sinistra (cioè ottenibile con operazioni di riga) a una e una sola matrice completamente ridotta a scala.

## Esempi

Da $\begin{pmatrix}2&4\\0&3\end{pmatrix}$ si normalizzano i pivot ottenendo $\begin{pmatrix}1&2\\0&1\end{pmatrix}$, poi $R_1\leftarrow R_1-2R_2$ dà $I_2$.

Una matrice invertibile si riduce sempre alla matrice identità.

## Come si dimostra

La costruzione è descritta [[2026-10-27 - Rango, sistemi lineari e matrici elementari#14. Forma completamente ridotta a scala|nella lezione del 27 ottobre]]. L'unicità della forma ridotta in ogni classe di equivalenza a sinistra è enunciata lì senza ulteriori dettagli.

## Vedi anche

- [[Matrice a scala]]
- [[Algoritmo di eliminazione di Gauss]]
- [[Matrice invertibile]]
- [[Relazione di equivalenza]]
