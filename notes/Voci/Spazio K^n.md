---
title: Spazio K^n
type: voce
categoria: oggetto
corsi:
- Geometria 1
introdotta_in: 2026-09-30 - Spazi vettoriali, esempi e sottospazi
alias:
- K^n
- R^n
- spazio delle n-uple
sintesi: Lo spazio K^n è l'insieme delle n-uple ordinate di elementi di un campo K, con somma e prodotto per scalare fatti componente per componente.
---

Lo **spazio $K^n$** è l'insieme delle $n$-uple ordinate di elementi di un [[Campo|campo]] $K$. È l'esempio fondamentale di [[Spazio vettoriale|spazio vettoriale]]: i casi più importanti sono $\mathbb{R}^n$ e $\mathbb{C}^n$.

## Definizione

$$
K^n=\{(x_1,\dots,x_n)\mid x_i\in K\}.
$$

Per $\mathbf x=(x_1,\dots,x_n)$, $\mathbf y=(y_1,\dots,y_n)$ e $\alpha\in K$:

$$
\mathbf x+\mathbf y=(x_1+y_1,\dots,x_n+y_n),
\qquad
\alpha\mathbf x=(\alpha x_1,\dots,\alpha x_n).
$$

Il vettore nullo è $\mathbf 0=(0,\dots,0)$ e l'opposto di $\mathbf x$ è $-\mathbf x=(-x_1,\dots,-x_n)$.

## Intuizione

Si fanno tutti i conti una coordinata alla volta, quindi ogni assioma si riduce al corrispondente assioma di $K$. Attenzione però a distinguere le operazioni: la somma tra vettori è nuova, quella tra scalari è già nel campo. Dopo la scelta di una base, ogni spazio di dimensione $n$ si comporta come $K^n$ (vedi [[Coordinate rispetto a una base]]).

## Esempi

- $\mathbb{R}^2$ è il piano cartesiano, $\mathbb{R}^3$ lo spazio.
- In $\mathbb{R}^3$: $(1,2,3)+(0,-1,4)=(1,1,7)$ e $2(1,2,3)=(2,4,6)$.
- La [[Base di uno spazio vettoriale|base canonica]] $e_1,\dots,e_n$ ha un $1$ nella posizione $i$ e zeri altrove.

## Come si dimostra

Per esempio l'associatività della somma discende da quella di $K$ componente per componente: vedi [[2026-09-30 - Spazi vettoriali, esempi e sottospazi#5.1 Associatività della somma|la verifica dell'associatività]].

## Vedi anche

- [[Spazio vettoriale]]
- [[Base di uno spazio vettoriale]]
- [[Dimensione di uno spazio vettoriale]]
- [[Matrice]]
