---
title: Numeri coprimi
type: voce
categoria: definizione
corsi:
- Aritmetica
introdotta_in: 2026-10-06 - Equazioni diofantee lineari e loro soluzioni
alias:
- coprimi
- relativamente primi
sintesi: Due interi sono coprimi se il loro massimo comun divisore è uno, cioè non hanno divisori comuni oltre a uno.
---

Due interi $a$ e $b$ sono **coprimi** (o primi tra loro) se non hanno fattori primi in comune.

## Definizione

$a$ e $b$ sono coprimi se $\gcd(a,b)=1$. Per l'[[Identità di Bézout]] questo equivale a

$$\exists\,u,v\in\mathbb{Z}:\ ua+vb=1.$$

Ogni coppia si può ridurre al caso coprimo dividendo per il MCD: $a=da_1$, $b=db_1$ con $\gcd(a_1,b_1)=1$.

## Intuizione

Coprimi non significa primi: $8$ e $15$ sono coprimi pur essendo entrambi composti. È la condizione sotto cui si può cancellare un fattore in una congruenza, avere un inverso modulo $n$ e applicare il [[Teorema cinese del resto]].

Una verifica pratica: per capire se due numeri sono coprimi basta eseguire l'algoritmo di Euclide e controllare che l'ultimo resto non nullo sia $1$. Se invece $\gcd(a,b)=d>1$, dividendo per $d$ si ottengono due numeri coprimi.

## Esempi

- $\gcd(45,17)=1$: coprimi.
- $\gcd(14,21)=7$: non coprimi.
- $a$ è invertibile modulo $n$ se e solo se $\gcd(a,n)=1$.

## Vedi anche

- [[Massimo comun divisore]]
- [[Identità di Bézout]]
- [[Lemma di Euclide]]
- [[Inverso modulo n]]
