---
title: Divisione euclidea
type: voce
categoria: teorema
corsi:
- Aritmetica
introdotta_in: 2026-10-05 - Divisione euclidea, massimo comun divisore e identità di Bézout
alias:
- teorema della divisione euclidea
- divisione con resto
sintesi: Dati due interi con il secondo non nullo, esistono un unico quoziente e un unico resto, con il resto non negativo e minore del valore assoluto del divisore.
---

La **divisione euclidea** (o divisione con resto) dice che dividere un intero $a$ per un intero $b\ne0$ produce in modo unico un quoziente e un resto "piccolo".

## Enunciato

Siano $a,b\in\mathbb{Z}$ con $b\ne0$. Esistono e sono unici $q,r\in\mathbb{Z}$ tali che

$$a=qb+r,\qquad 0\le r<|b|.$$

$q$ è il *quoziente*, $r$ il *resto*. La condizione $0\le r<|b|$ è essenziale per l'unicità: senza di essa si potrebbe sostituire $q$ con $q+1$ e $r$ con $r-b$.

## Intuizione

Approssimi $a$ con un multiplo di $b$ senza sforare per eccesso: il resto è ciò che rimane. È lo strumento di base dell'aritmetica: da qui nascono l'[[Algoritmo di Euclide]], il [[Massimo comun divisore]] e le [[Congruenza modulo n|congruenze]].

## Esempi

- $45=2\cdot17+11$.
- $-17=(-4)\cdot5+3$: il resto è $3$, non $-2$.
- Con $b<0$, ad esempio $17=(-3)\cdot(-5)+2$ (resto compreso tra $0$ e $|b|-1$).

## Come si dimostra

*Esistenza* (caso $b>0$): l'insieme $\{a-qb\ge0\}$ è non vuoto e per il [[Principio del minimo]] ha un minimo $r$; se fosse $r\ge b$, allora $r-b$ sarebbe un elemento più piccolo. *Unicità*: da $(q_1-q_2)b=r_2-r_1$ segue $q_1=q_2$. Vedi [[2026-10-05 - Divisione euclidea, massimo comun divisore e identità di Bézout#3. Dimostrazione dell’esistenza|la lezione del 5 ottobre]].

## Vedi anche

- [[Algoritmo di Euclide]]
- [[Divisibilità]]
- [[Principio del minimo]]
- [[Congruenza modulo n]]
