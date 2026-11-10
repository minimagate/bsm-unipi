---
title: Massimo e minimo
type: voce
categoria: definizione
corsi:
- Analisi 1
introdotta_in: 2026-09-28 - Assiomi dei reali e proprietà di completezza
alias:
- massimo
- minimo
sintesi: Il massimo di un insieme è un suo elemento che è anche maggiorante, il minimo è un suo elemento che è anche minorante; se esistono sono unici.
---
Il **massimo** di $A\subseteq\mathbb{R}$ è un elemento di $A$ maggiore o uguale a tutti gli altri; il **minimo** è un elemento di $A$ minore o uguale a tutti gli altri.

## Definizione

$$
M=\max A\iff M\in A\ \text{e}\ \forall a\in A,\ a\le M,
$$

$$
m=\min A\iff m\in A\ \text{e}\ \forall a\in A,\ m\le a.
$$

In altre parole, il massimo è un [[Maggiorante|maggiorante]] che appartiene all'insieme.

## Intuizione

Massimo e minimo **non sono obbligati a esistere**. Se esistono sono unici: se $M_1$ e $M_2$ sono due massimi, allora $M_2\le M_1$ e $M_1\le M_2$, quindi $M_1=M_2$ per antisimmetria dell'ordine.

## Esempi

- $\max[0,1]=1$ e $\min[0,1]=0$.
- $(0,1)$ non ha né massimo né minimo: $1$ e $0$ sono barriere ma non appartengono all'insieme.
- Se il massimo esiste coincide con l'[[Estremo superiore|estremo superiore]].

## Come si dimostra

L'unicità è mostrata nella sezione [[2026-09-28 - Assiomi dei reali e proprietà di completezza#11. Maggioranti, minoranti, massimo e minimo|Maggioranti, minoranti, massimo e minimo]] della lezione.

## Vedi anche

- [[Maggiorante]]
- [[Estremo superiore]]
- [[Assioma di completezza]]
