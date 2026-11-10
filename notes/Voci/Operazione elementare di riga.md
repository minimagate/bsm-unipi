---
title: Operazione elementare di riga
type: voce
categoria: definizione
corsi:
- Geometria 1
introdotta_in: 2026-10-22 - Sistemi lineari e algoritmo di eliminazione di Gauss
alias:
- operazioni elementari di riga
- operazioni elementari
sintesi: Una delle tre trasformazioni delle righe di una matrice (scambio, moltiplicazione per uno scalare non nullo, somma di un multiplo di un'altra riga) che non cambiano le soluzioni del sistema.
---

Le **operazioni elementari di riga** sono le tre trasformazioni delle righe di una matrice che conservano le soluzioni del sistema lineare associato. Sono lo strumento di base dell'eliminazione di Gauss.

## Definizione

Sulle righe di una matrice (o di una matrice completa) sono ammesse:

1. scambiare due righe;
2. moltiplicare una riga per uno scalare $\lambda\neq 0$;
3. sostituire una riga $R_j$ con $R_j+\lambda R_k$, con $k\neq j$.

Ognuna è invertibile: si torna indietro con lo stesso scambio, con $\lambda^{-1}$, oppure con $R_j-\lambda R_k$.

## Intuizione

Sono le mosse che si fanno a mano quando si risolve un sistema: riordinare le equazioni, riscalare un'equazione, sommare a un'equazione un multiplo di un'altra. Poiché sono reversibili, non si perde né si inventa informazione. Occhio a $\lambda\neq 0$: moltiplicare per zero distrugge l'equazione.

## Esempi

Nella matrice completa $\left(\begin{array}{cc|c}1&2&3\\2&5&7\end{array}\right)$ la mossa $R_2\leftarrow R_2-2R_1$ dà $\left(\begin{array}{cc|c}1&2&3\\0&1&1\end{array}\right)$, con le stesse soluzioni.

Le operazioni di riga cambiano le colonne (e il loro span) ma non lo span delle righe: perciò preservano il rango.

## Come si dimostra

L'invarianza dell'insieme delle soluzioni e dello span delle righe è discussa [[2026-10-22 - Sistemi lineari e algoritmo di eliminazione di Gauss#5. Invarianza dell’insieme delle soluzioni|nella lezione del 22 ottobre]]. Ogni operazione equivale a una moltiplicazione a sinistra per una matrice elementare.

## Vedi anche

- [[Algoritmo di eliminazione di Gauss]]
- [[Matrice elementare]]
- [[Matrice a scala]]
- [[Rango]]
