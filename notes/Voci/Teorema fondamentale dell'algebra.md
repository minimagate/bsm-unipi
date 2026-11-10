---
title: Teorema fondamentale dell'algebra
type: voce
categoria: teorema
corsi:
- Geometria 1
introdotta_in: 2026-09-25 - Numeri complessi- operazioni, forma polare e radici
alias:
- teorema fondamentale dell'algebra complessa
sintesi: Ogni polinomio non costante a coefficienti complessi ha almeno una radice complessa.
---

Il **teorema fondamentale dell'algebra** afferma che i [[Numero complesso|numeri complessi]] sono un campo sufficientemente grande da contenere una radice di ogni [[Polinomio|polinomio]] non costante.

## Enunciato

Se $P(z)\in\mathbb{C}[z]$ ha grado almeno $1$, allora esiste $z_0\in\mathbb{C}$ tale che $P(z_0)=0$.

Applicato ripetutamente (togliendo ogni volta il fattore $z-z_0$) dà la fattorizzazione completa:

$$
P(z)=a_n(z-z_1)(z-z_2)\cdots(z-z_n),
$$

dove $z_1,\dots,z_n$ sono le radici contate con molteplicità.

## Intuizione

Nei reali non basta: $x^2+1$ non ha radici reali. Nei complessi ha $i$ e $-i$. Il teorema dice che, una volta passati a $\mathbb{C}$, non serve estendere ancora il campo per risolvere equazioni polinomiali. Non dice che le radici siano distinte: una stessa radice può comparire più volte (vedi [[Radice di un polinomio]]).

## Esempi

- $z^2+1=(z-i)(z+i)$.
- $z^n=w$ con $w\neq 0$ ha $n$ soluzioni distinte: sono le [[Radice n-esima di un numero complesso|radici n-esime]] di $w$.
- $(z-1)^5$ ha una sola radice distinta, $1$, con molteplicità $5$.

## Come si dimostra

Nel corso la dimostrazione del teorema arriva più avanti. La sua conseguenza, la fattorizzazione in fattori lineari, si prova per induzione sul grado: vedi [[2026-10-01 - Fattorizzazione dei polinomi e radici complesse#2. Corollario: fattorizzazione completa in fattori lineari|il corollario nella lezione del 1 ottobre]].

## Vedi anche

- [[Polinomio]]
- [[Radice di un polinomio]]
- [[Numero complesso]]
- [[Principio di induzione]]
