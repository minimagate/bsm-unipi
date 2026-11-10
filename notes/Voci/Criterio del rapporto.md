---
title: Criterio del rapporto
type: voce
categoria: teorema
corsi:
- Analisi 1
introdotta_in: 2026-10-08 - Criteri della radice e del rapporto e gerarchia degli infiniti
sintesi: Se il rapporto tra termini consecutivi di una successione positiva ha limite maggiore di uno la successione diverge, se minore di uno tende a zero.
---
Il **criterio del rapporto** studia il comportamento di una successione positiva guardando il rapporto tra due termini consecutivi.

## Enunciato

Sia $a_n>0$ definitivamente e $\frac{a_{n+1}}{a_n}\to\ell\in[0,+\infty]$.

- Se $\ell>1$, allora $a_n\to+\infty$.
- Se $\ell<1$, allora $a_n\to0$.
- Se $\ell=1$, il criterio **non** permette di concludere.

Vale anche un teorema più forte, **rapporto $\Rightarrow$ radice**: se $\frac{a_{n+1}}{a_n}\to\ell$ allora $\sqrt[n]{a_n}\to\ell$. Il viceversa è falso (per $1,2,1,2,\dots$ la radice tende a $1$ ma il rapporto non ha limite).

## Intuizione

Se ogni termine è almeno $q>1$ volte il precedente, la successione cresce almeno come una progressione geometrica; se è al più $q<1$ volte, decresce come una progressione geometrica. Quando il rapporto tra termini consecutivi è semplice, conviene usare questo criterio (anche per calcolare limiti di radici).

## Esempi

- $\frac{3^n}{n^{78}}$: il rapporto tende a $3>1$, quindi la successione $\to+\infty$.
- $\frac{n!}{3^n}$: il rapporto è $\frac{n+1}3\to+\infty$.
- $\frac{n^n}{n!}$: il rapporto è $\left(1+\frac1n\right)^n\to e>1$.
- $\sqrt[n]{\binom{3n}{n}}\to\frac{27}4$.

## Come si dimostra

Definitivamente $a_{n+1}\ge q\,a_n$ (con $q>1$), dunque iterando $a_n\ge q^{n-n_0}a_{n_0}\to+\infty$; il caso $\ell<1$ è analogo con $a_n\le q^{n-n_0}a_{n_0}\to0$. Si veda [[2026-10-08 - Criteri della radice e del rapporto e gerarchia degli infiniti#4. Criterio del rapporto|Criterio del rapporto]].

## Vedi anche

- [[Criterio della radice]]
- [[Gerarchia degli infiniti]]
- [[Numero di Nepero]]
- [[Limite di una successione]]
