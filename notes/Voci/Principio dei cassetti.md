---
title: Principio dei cassetti
type: voce
categoria: teorema
corsi:
- Aritmetica
introdotta_in: 2026-09-29 - Cardinalità e tecniche fondamentali del calcolo combinatorio
alias:
- pigeonhole
sintesi: Se si distribuiscono più oggetti che cassetti, almeno un cassetto ne contiene due o più.
---

Il **principio dei cassetti** (o di Dirichlet, o della piccionaia) è un'osservazione semplice ma potente sui conteggi di insiemi finiti.

## Enunciato

Se si distribuiscono $n$ oggetti in $k$ cassetti con $n>k$, almeno un cassetto contiene almeno due oggetti. In forma funzionale: se $|X|>|Y|$, una funzione $f:X\to Y$ non può essere iniettiva.

## Intuizione

Se hai $10$ calzini e $7$ cassetti, per forza due calzini finiscono nello stesso cassetto. Il principio non dice *quale* cassetto, ma garantisce che una coincidenza avviene: per questo serve a mostrare che certe cose sono impossibili.

## Esempi

- $10$ oggetti in $7$ cassetti: almeno un cassetto ne contiene due.
- Non esistono funzioni iniettive da un insieme di $5$ elementi a uno di $3$: il numero di funzioni iniettive $\frac{m!}{(m-n)!}$ vale $0$ se $n>m$.

## Come si dimostra

Se $f$ fosse iniettiva, elementi distinti di $X$ avrebbero immagini distinte, quindi $|Y|\ge|X|$: contraddizione. Vedi [[2026-09-29 - Cardinalità e tecniche fondamentali del calcolo combinatorio#5. Il principio dei cassetti|la lezione]].

## Vedi anche

- [[Cardinalità]]
- [[Funzione biettiva]]
- [[Double counting]]
