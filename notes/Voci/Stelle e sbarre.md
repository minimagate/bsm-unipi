---
title: Stelle e sbarre
type: voce
categoria: metodo
corsi:
- Aritmetica
introdotta_in: 2026-10-13 - Divisori, algoritmo di Euclide e conteggio combinatorio
alias:
- stars and bars
sintesi: Metodo per contare le soluzioni intere non negative di un'equazione somma, disponendo stelle e sbarre su una riga.
---

Il metodo delle **stelle e sbarre** (*stars and bars*) conta in quanti modi si può distribuire una quantità tra più variabili intere non negative.

## Enunciato

Il numero di soluzioni intere non negative di

$$u_1+u_2+\cdots+u_r=n$$

è

$$\binom{n+r-1}{r-1}.$$

Si dispongono $n$ stelle e $r-1$ sbarre: le stelle prima della prima sbarra danno $u_1$, quelle tra la prima e la seconda danno $u_2$, e così via.

## Intuizione

Una soluzione corrisponde a una riga di $n+r-1$ simboli in cui scegli quali $r-1$ posizioni sono sbarre: ecco il [[Coefficiente binomiale]]. Il numero di sbarre è sempre il numero di variabili meno uno.

## Esempi

- $\alpha_1+\beta_1+\gamma_1=4$: $\binom{6}{2}=15$; $\alpha_2+\beta_2+\gamma_2=3$: $\binom52=10$; le terne $(x,y,z)$ con $xyz=2000$ sono $15\cdot10=150$.
- Per interi positivi si pone $a'=a-1\ge0$: $a+b+c=100$ diventa $a'+b'+c'=97$, con $\binom{99}{2}=4851$ soluzioni.

## Come si dimostra

Vedi [[2026-10-13 - Divisori, algoritmo di Euclide e conteggio combinatorio#Metodo delle stelle e sbarre|la lezione del 13 ottobre]].

## Vedi anche

- [[Coefficiente binomiale]]
- [[Coefficiente multinomiale]]
- [[Teorema fondamentale dell'aritmetica]]
- [[Double counting]]
