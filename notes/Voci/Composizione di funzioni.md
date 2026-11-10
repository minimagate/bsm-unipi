---
title: Composizione di funzioni
type: voce
categoria: definizione
corsi:
- Analisi 1
- Aritmetica
- Geometria 1
introdotta_in: 2026-09-23 - Insiemi, applicazioni e spazi vettoriali
alias:
- composizione
- funzione composta
- applicazione composta
sintesi: La composizione di due funzioni applica prima la prima e poi la seconda, ottenendo una nuova funzione.
---

La **composizione** di due [[Funzione|funzioni]] $f:X\to Y$ e $g:Y\to Z$ è la funzione $g\circ f:X\to Z$ che applica prima $f$ e poi $g$.

## Definizione

Se il codominio di $f$ è il dominio di $g$, si pone

$$
(g\circ f)(x)=g(f(x)).
$$

La composizione è associativa: $h\circ(g\circ f)=(h\circ g)\circ f$ quando le funzioni sono componibili. L'elemento neutro è l'applicazione identica $\operatorname{id}_X(x)=x$.

## Intuizione

Si leggono le funzioni da destra a sinistra, come nella scrittura $g(f(x))$: la più vicina a $x$ agisce per prima. In generale $g\circ f\neq f\circ g$ (e spesso una delle due nemmeno ha senso).

## Esempi

Con $f(x)=x+1$ e $g(x)=x^2$ da $\mathbb{R}$ a $\mathbb{R}$:

- $(g\circ f)(x)=(x+1)^2$,
- $(f\circ g)(x)=x^2+1$.

Sono funzioni diverse: l'ordine conta. Se invece $f$ e $g$ fossero definite su insiemi che non si "incastrano" (il codominio di $f$ diverso dal dominio di $g$), la composizione $g\circ f$ non avrebbe nemmeno senso.

Un altro caso utile: se $f$ è biettiva con inversa $f^{-1}$, allora $f^{-1}\circ f=\operatorname{id}_X$ e $f\circ f^{-1}=\operatorname{id}_Y$. In geometria lineare, comporre due applicazioni lineari dà ancora un'applicazione lineare, e al prodotto di matrici corrisponde proprio la composizione.

## Vedi anche

- [[Funzione]]
- [[Funzione inversa]]
- [[Funzione biettiva]]
- [[Applicazione lineare]]
