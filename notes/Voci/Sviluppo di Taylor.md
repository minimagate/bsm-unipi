---
title: Sviluppo di Taylor
type: voce
categoria: teorema
corsi:
- Analisi 1
introdotta_in: 2026-10-28 - Teorema di De L'Hôpital e sviluppi di Taylor
alias:
- Taylor
- polinomio di Taylor
- Taylor-Peano
- teorema di Taylor-Peano
- McLaurin
- sviluppi di Taylor
sintesi: Una funzione sufficientemente regolare si approssima vicino a un punto con un polinomio, calcolato dalle sue derivate, a meno di un errore trascurabile.
---

Lo **sviluppo di Taylor** (con il resto di Peano) approssima una funzione vicino a un punto con un polinomio di grado $n$, i cui coefficienti si leggono dalle derivate nel punto. Nel centro $0$ si parla di sviluppo di McLaurin.

## Enunciato

Sia $f:(-\delta,\delta)\to\mathbb R$ derivabile $n-1$ volte in $(-\delta,\delta)$ e $n$ volte in $0$. Allora per $x\to0$

$$
f(x)=\sum_{k=0}^n\frac{f^{(k)}(0)}{k!}x^k+o(x^n).
$$

Il polinomio $P_n$ con questa proprietà (grado $\le n$ e resto $o(x^n)$) è **unico**. Con centro $x_0$ si scrive $f(x)=\sum_{k=0}^m\frac{f^{(k)}(x_0)}{k!}(x-x_0)^k+o\bigl((x-x_0)^m\bigr)$.

## Intuizione

Si approssima la funzione con un polinomio, che è facile da trattare, pagando un errore piccolo: un [[Simboli di Landau|$o(x^n)$]]. Con $n=1$ si ottiene la [[Differenziabilità|differenziabilità]], con $n=0$ la continuità.

Sviluppi fondamentali per $x\to0$:

$$
e^x=\sum\frac{x^k}{k!},\quad \sin x=x-\frac{x^3}{3!}+\frac{x^5}{5!}-\dots,\quad \cos x=1-\frac{x^2}{2!}+\frac{x^4}{4!}-\dots,
$$

$$
\log(1+x)=x-\frac{x^2}2+\frac{x^3}3-\dots,\quad \arctan x=x-\frac{x^3}3+\frac{x^5}5-\dots,\quad (1+x)^a=\sum\binom ak x^k.
$$

## Esempi

- $\cos x=1-\frac{x^2}2+o(x^2)$ perché $f(0)=1$, $f'(0)=0$, $f''(0)=-1$.
- $\dfrac1{1+x}=1-x+x^2-x^3+\dots$ (caso $a=-1$ del binomio).
- Lo sviluppo di una funzione pari ha solo potenze pari, quello di una dispari solo potenze dispari.

## Come si dimostra

Il teorema di Taylor–Peano è enunciato senza dimostrazione nel corso; l'unicità del polinomio si dimostra per assurdo guardando il termine di grado minimo della differenza (vedi la [[2026-10-28 - Teorema di De L'Hôpital e sviluppi di Taylor#2. Il problema di Taylor–McLaurin|lezione del 28 ottobre]]).

## Vedi anche

- [[Simboli di Landau]]
- [[Derivata]]
- [[Parte principale]]
- [[Teorema di De L'Hôpital]]
