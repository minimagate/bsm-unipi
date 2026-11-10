---
title: Massimo comun divisore
type: voce
categoria: definizione
corsi:
- Aritmetica
- Fondamenti di Programmazione
introdotta_in: 2026-10-05 - Divisione euclidea, massimo comun divisore e identità di Bézout
alias:
- MCD
- massimo comune divisore
- gcd
sintesi: Il massimo comun divisore di due interi è il più grande intero positivo che divide entrambi.
---

Il **massimo comun divisore** (MCD, in inglese $\gcd$) di due interi $a,b$, non entrambi nulli, è il più grande divisore comune positivo di $a$ e $b$.

## Definizione

Equivalentemente, $\gcd(a,b)$ è l'unico intero positivo $d$ tale che:

1. $d\mid a$ e $d\mid b$;
2. ogni divisore comune di $a$ e $b$ divide $d$.

Esiste sempre (i divisori comuni positivi sono un insieme finito non vuoto, contiene $1$), è unico e $\gcd(a,b)=\gcd(|a|,|b|)$. Si calcola con l'[[Algoritmo di Euclide]] e vale l'[[Identità di Bézout]]. Se $\gcd(a,b)=1$ i numeri sono [[Numeri coprimi]].

## Intuizione

La seconda formulazione è quella davvero utile: il MCD non è solo il più grande, ma è anche "divisibile da tutti" i divisori comuni. Con la fattorizzazione, $\gcd(A,B)=\prod p_i^{\min(\alpha_i,\beta_i)}$.

## Esempi

- $\gcd(45,17)=1$.
- $\gcd(12,18)=6$.
- $\gcd(a,0)=|a|$.

## Come si dimostra

L'esistenza e le proprietà sono nella [[2026-10-05 - Divisione euclidea, massimo comun divisore e identità di Bézout#7. Massimo comun divisore|lezione del 5 ottobre]]; il calcolo con gli esponenti primi è nella lezione del 13 ottobre.

## Vedi anche

- [[Algoritmo di Euclide]]
- [[Identità di Bézout]]
- [[Minimo comune multiplo]]
- [[Numeri coprimi]]
- [[Divisibilità]]
