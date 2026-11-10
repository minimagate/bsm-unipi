---
title: Coefficiente binomiale
type: voce
categoria: definizione
corsi:
- Aritmetica
introdotta_in: 2026-09-29 - Cardinalità e tecniche fondamentali del calcolo combinatorio
alias:
- coefficienti binomiali
sintesi: Il coefficiente binomiale n su r è il numero di sottoinsiemi di r elementi di un insieme di n elementi.
---

Il **coefficiente binomiale** $\binom{n}{r}$ (si legge "$n$ su $r$") conta i sottoinsiemi di $r$ elementi di un insieme di $n$ elementi.

## Definizione

Per $0\le r\le n$,

$$\binom{n}{r}=\frac{n!}{r!\,(n-r)!}.$$

Valgono $\binom{n}{0}=\binom{n}{n}=1$, la simmetria $\binom{n}{r}=\binom{n}{n-r}$ e, per convenzione, $\binom{n}{r}=0$ se $r<0$ o $r>n$. L'identità di Pascal è $\binom{n}{j-1}+\binom{n}{j}=\binom{n+1}{j}$.

## Intuizione

Si contano prima le $r$-uple *ordinate* di elementi distinti, $\frac{n!}{(n-r)!}$, e poi si divide per $r!$, perché ogni sottoinsieme è stato contato una volta per ciascun ordinamento dei suoi elementi.

Per questo $\binom{n}{r}$ è sempre un intero, anche se è scritto come frazione di fattoriali. Si ritrova nel triangolo di Pascal, dove ogni numero è la somma dei due sopra di lui.

## Esempi

- $\binom{5}{2}=\frac{5\cdot 4}{2}=10$.
- $\binom{n}{r}=\binom{n}{n-r}$: scegliere $r$ elementi equivale a scegliere i $n-r$ da lasciare fuori (complementare).
- Compaiono come coefficienti nel [[Binomio di Newton]].

## Come si dimostra

Vedi [[2026-09-29 - Cardinalità e tecniche fondamentali del calcolo combinatorio#13. Sottoinsiemi di cardinalità fissata e coefficienti binomiali|la lezione del 29 settembre]].

## Vedi anche

- [[Binomio di Newton]]
- [[Insieme delle parti]]
- [[Coefficiente multinomiale]]
- [[Stelle e sbarre]]
