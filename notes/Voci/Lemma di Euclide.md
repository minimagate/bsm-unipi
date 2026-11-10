---
title: Lemma di Euclide
type: voce
categoria: teorema
corsi:
- Aritmetica
introdotta_in: 2026-10-06 - Equazioni diofantee lineari e loro soluzioni
alias:
- lemma di Euclide sui primi
sintesi: Se un intero è coprimo con un altro e divide un loro prodotto, allora divide l'altro fattore.
---

Il **lemma di Euclide** è la proprietà che permette di "semplificare" un fattore coprimo in una relazione di divisibilità.

## Enunciato

Se $\gcd(r,s)=1$ e $r\mid st$, allora $r\mid t$. In particolare, se un [[Numero primo]] $p$ divide un prodotto $st$, allora $p\mid s$ oppure $p\mid t$.

## Intuizione

Se $r$ non ha fattori in comune con $s$, tutto ciò che serve a $r$ per dividere $st$ deve stare in $t$. È proprio l'ingrediente che rende *unica* la fattorizzazione in primi.

## Esempi

- $4\mid 3\cdot 8$ e $\gcd(4,3)=1$, quindi $4\mid8$.
- $6\mid 4\cdot 9$ ma $6\nmid4$ e $6\nmid9$: la tesi cade perché $6$ non è primo e non è coprimo né con $4$ né con $9$.

## Come si dimostra

Per la [[Identità di Bézout]] esistono $u,v$ con $ur+vs=1$; moltiplicando per $t$ si ha $t=urt+vst$, e $r$ divide entrambi gli addendi. Il lemma è usato nella [[2026-10-06 - Equazioni diofantee lineari e loro soluzioni#7. Lemma di Euclide|lezione del 6 ottobre]].

## Vedi anche

- [[Numeri coprimi]]
- [[Identità di Bézout]]
- [[Teorema fondamentale dell'aritmetica]]
- [[Equazione diofantea lineare]]
