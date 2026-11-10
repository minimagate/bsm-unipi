---
title: Successione di Fibonacci
type: voce
categoria: oggetto
corsi:
- Aritmetica
- Fondamenti di Programmazione
introdotta_in: 2026-09-30 - Successioni ricorrenti e formule combinatorie
alias:
- Fibonacci
- numeri di Fibonacci
sintesi: Successione in cui ogni termine è la somma dei due precedenti, a partire da zero e uno.
---

La **successione di Fibonacci** è definita da $F_{n+1}=F_n+F_{n-1}$ con $F_0=0$ e $F_1=1$: ogni numero è la somma dei due precedenti.

## Definizione

$$F_0=0,\quad F_1=1,\quad F_{n+1}=F_n+F_{n-1}.$$

I primi termini sono $0,1,1,2,3,5,8,13,\ldots$ Risolvendo la [[Successione per ricorrenza|ricorrenza]] con $\lambda^2-\lambda-1=0$ si trovano $\varphi=\frac{1+\sqrt5}{2}$ e $\psi=\frac{1-\sqrt5}{2}$ e la formula esplicita

$$F_n=\frac{\varphi^n-\psi^n}{\sqrt5}.$$

## Intuizione

Pur essendo definita con sole somme, ha una formula chiusa che coinvolge $\sqrt5$. Compare spesso nei conteggi, perché molti problemi si spezzano in "un passo" o "due passi".

## Esempi

Le tassellazioni di una griglia $2\times n$ con tessere $2\times1$ sono $T_n=T_{n-1}+T_{n-2}$ con $T_0=T_1=1$, quindi $T_n=F_{n+1}$: $1,2,3,5,8,\ldots$ Si ottiene anche $T_n=\sum_{k}\binom{n-k}{k}$.

## Come si dimostra

Vedi [[2026-09-30 - Successioni ricorrenti e formule combinatorie#5. Collegamento con la successione di Fibonacci|la lezione del 30 settembre]] e [[2026-10-07 - Conteggio combinatorio e principio di inclusione-esclusione#8. Tassellazioni di una griglia $2\times n$|le tassellazioni del 7 ottobre]].

## Vedi anche

- [[Successione per ricorrenza]]
- [[Coefficiente binomiale]]
- [[Double counting]]
