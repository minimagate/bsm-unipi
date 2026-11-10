---
title: Identità di Bézout
type: voce
categoria: teorema
corsi:
- Aritmetica
introdotta_in: 2026-10-05 - Divisione euclidea, massimo comun divisore e identità di Bézout
alias:
- Bézout
- coefficienti di Bézout
sintesi: Il massimo comun divisore di due interi si scrive come loro combinazione lineare a coefficienti interi.
---

L'**identità di Bézout** afferma che il [[Massimo comun divisore]] di due interi è una combinazione lineare intera di essi.

## Enunciato

Per ogni $a,b\in\mathbb{Z}$ non entrambi nulli esistono $u,v\in\mathbb{Z}$ tali che

$$\gcd(a,b)=ua+vb.$$

In particolare $\gcd(a,b)=1$ se e solo se esistono $u,v$ con $ua+vb=1$.

## Intuizione

Gli interi della forma $ua+vb$ sono tutti multipli del MCD, e il MCD stesso si ottiene. È la chiave per risolvere le [[Equazione diofantea lineare|equazioni diofantee]] e per calcolare gli [[Inverso modulo n|inversi modulari]].

## Esempi

Da $45=2\cdot17+11$, $17=11+6$, $11=6+5$, $6=5+1$, risalendo si trova

$$1=8\cdot17-3\cdot45.$$

## Come si dimostra

Ogni resto dell'[[Algoritmo di Euclide]] è combinazione lineare di $a$ e $b$, quindi lo è anche l'ultimo resto non nullo, cioè il MCD; i coefficienti si ricavano risalendo le divisioni. Vedi [[2026-10-05 - Divisione euclidea, massimo comun divisore e identità di Bézout#12. Dimostrazione mediante l’algoritmo di Euclide|la lezione del 5 ottobre]].

## Vedi anche

- [[Massimo comun divisore]]
- [[Algoritmo di Euclide]]
- [[Equazione diofantea lineare]]
- [[Inverso modulo n]]
- [[Numeri coprimi]]
