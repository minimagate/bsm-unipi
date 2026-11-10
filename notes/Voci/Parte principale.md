---
title: Parte principale
type: voce
categoria: definizione
corsi:
- Analisi 1
introdotta_in: 2026-10-29 - Operazioni con Taylor e parti principali
alias:
- ordine di infinitesimo
- parte principale di una funzione
sintesi: Il primo termine che resta in uno sviluppo dopo le eventuali cancellazioni, cioè il pezzo che descrive il comportamento della funzione vicino al punto.
---

La **parte principale** di una funzione è il termine che "comanda" vicino a un punto: quello di grado più basso che sopravvive agli sviluppi e alle cancellazioni.

## Definizione

Se per $x\to0$

$$
f(x)\sim ax^b,\quad a\neq0,\qquad\text{cioè}\qquad f(x)=ax^b+o(x^b),
$$

il termine $ax^b$ si chiama **parte principale** di $f$. Se $b>0$, $f$ è un infinitesimo e $b$ è il suo **ordine** (di infinitesimo) rispetto a $x$.

## Intuizione

Con Taylor la parte principale è il **primo monomio non nullo** dello sviluppo, contando dal grado più basso dopo le cancellazioni. Serve a risolvere limiti in cui i termini lineari (o di grado più basso) si cancellano: bisogna spingersi fino all'ordine in cui compare davvero qualcosa.

## Esempi

- $\sin x-\arctan x=\frac{x^3}6+o(x^3)$: gli sviluppi lineari si cancellano, la parte principale è $\frac{x^3}6$ e l'ordine è $3$.
- Quindi $\displaystyle\lim_{x\to0}\frac{\sin x-\arctan x}{e^{x^3}-1}=\frac{x^3/6}{x^3}=\frac16$.
- $\dfrac1{\sin x}-\dfrac1x=\dfrac x6+o(x)$, e $\sqrt{n+1}-\sqrt n=\dfrac1{2\sqrt n}+o\!\left(\dfrac1{\sqrt n}\right)$ per $n\to+\infty$.

## Come si dimostra

Non è un teorema ma una definizione: il calcolo si fa con gli sviluppi, come nella [[2026-10-29 - Operazioni con Taylor e parti principali#4. Parte principale e ordine di infinitesimo|lezione del 29 ottobre]].

## Vedi anche

- [[Sviluppo di Taylor]]
- [[Equivalenza asintotica]]
- [[Simboli di Landau]]
- [[Limiti notevoli]]
