---
title: Matrice a scala
type: voce
categoria: definizione
corsi:
- Geometria 1
introdotta_in: 2026-10-22 - Sistemi lineari e algoritmo di eliminazione di Gauss
alias:
- matrici a scala
- forma a scala
- pivot
sintesi: Matrice in cui la prima entrata non nulla di ogni riga sta più a destra di quella della riga precedente e le righe nulle sono in fondo.
---

Una **matrice a scala** è una matrice con una struttura "a gradini" che rende immediato risolvere il sistema lineare associato. Le prime entrate non nulle delle righe si chiamano **pivot**.

## Definizione

Una matrice è in forma a scala se:

1. le righe nulle, se ci sono, stanno in fondo;
2. in ogni riga non nulla la prima entrata non nulla (il pivot) si trova più a destra del pivot della riga precedente;
3. sotto ogni pivot ci sono solo zeri.

Gli elementi a destra o sopra i pivot possono essere qualsiasi.

## Intuizione

I pivot disegnano una scala che scende verso destra. Le colonne con un pivot corrispondono alle variabili "pivot", determinate dalle equazioni; le colonne senza pivot corrispondono alle variabili libere, che fanno da parametri. Il numero di pivot è il rango della matrice.

## Esempi

La matrice
$$
\begin{pmatrix}
1&2&0&3\\
0&0&1&-1\\
0&0&0&0
\end{pmatrix}
$$
è a scala, con pivot nella prima e nella terza colonna.

La matrice $\begin{pmatrix}1&2\\0&1\\0&1\end{pmatrix}$ non è a scala: le righe 2 e 3 hanno il pivot nella stessa colonna.

## Come si dimostra

Ogni matrice si può portare in forma a scala con operazioni elementari di riga: è il contenuto dell'algoritmo di Gauss. La definizione è data [[2026-10-22 - Sistemi lineari e algoritmo di eliminazione di Gauss#2.1 Definizione di matrice a scala|nella lezione del 22 ottobre]].

## Vedi anche

- [[Algoritmo di eliminazione di Gauss]]
- [[Operazione elementare di riga]]
- [[Forma ridotta a scala]]
- [[Rango]]
