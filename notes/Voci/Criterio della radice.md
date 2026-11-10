---
title: Criterio della radice
type: voce
categoria: teorema
corsi:
- Analisi 1
introdotta_in: 2026-10-08 - Criteri della radice e del rapporto e gerarchia degli infiniti
sintesi: Se la radice n-esima di una successione positiva ha limite maggiore di uno la successione diverge, se ha limite minore di uno tende a zero.
---
Il **criterio della radice** permette di capire se una successione positiva tende a $0$ o a $+\infty$ guardando il limite di $\sqrt[n]{a_n}$.

## Enunciato

Sia $a_n\ge0$ definitivamente e $\sqrt[n]{a_n}\to\ell\in[0,+\infty]$.

- Se $\ell>1$, allora $a_n\to+\infty$.
- Se $\ell<1$, allora $a_n\to0$.
- Se $\ell=1$, il criterio **non** permette di concludere.

## Intuizione

Se $\sqrt[n]{a_n}\approx\ell$ allora $a_n\approx\ell^n$: una potenza con base maggiore di $1$ esplode, con base minore di $1$ si spegne. Il valore $1$ è la soglia: è il caso di equilibrio in cui non si può dire nulla.

## Esempi

- $a_n=\frac{3^{n^2}}{n^n}$: $\sqrt[n]{a_n}=\frac{3^n}{n}\to+\infty$, quindi $a_n\to+\infty$.
- Limiti di base: $\sqrt[n]{a}\to1$ per ogni $a>0$ e $\sqrt[n]{n}\to1$ (da qui $\sqrt[n]{\text{polinomio positivo}}\to1$).
- $\sqrt[n]{7^n-n^7+n^5\cos(n!)}\to7$.

## Come si dimostra

Se $\ell>1$ si sceglie $q=\frac{\ell+1}2>1$: definitivamente $\sqrt[n]{a_n}\ge q$, cioè $a_n\ge q^n\to+\infty$ (confronto). Se $\ell<1$ si ha $0\le a_n\le q^n\to0$ e si usa il [[Teorema dei carabinieri|teorema dei carabinieri]]. Si veda [[2026-10-08 - Criteri della radice e del rapporto e gerarchia degli infiniti#3. Criterio della radice|Criterio della radice]].

## Vedi anche

- [[Criterio del rapporto]]
- [[Gerarchia degli infiniti]]
- [[Teorema dei carabinieri]]
- [[Limite di una successione]]
