---
title: Sviluppo decimale
type: voce
categoria: definizione
corsi:
- Aritmetica
introdotta_in: 2026-10-14 - Sviluppi decimali razionali e fattorizzazione dei denominatori
alias:
- sviluppi decimali
- sviluppo decimale periodico
sintesi: Rappresentazione di un numero reale come somma di cifre decimali, finita o infinita; è eventualmente periodica se e solo se il numero è razionale.
---

Lo **sviluppo decimale** di un numero reale $x\ge0$ lo scrive come parte intera più una successione di cifre decimali: $x=a_0,a_1a_2a_3\ldots$

## Definizione

$$x=a_0+\frac{a_1}{10}+\frac{a_2}{10^2}+\cdots,\qquad a_0\in\mathbb{Z}_{\ge0},\ a_i\in\{0,\ldots,9\}.$$

È *eventualmente periodico* se ha la forma $a_0,a_1\cdots a_s\overline{b_1\cdots b_n}$. Teorema: $x\in\mathbb{Q}$ se e solo se lo sviluppo decimale di $x$ è eventualmente periodico.

## Intuizione

Dividendo $a$ per $b$ ci sono solo $b$ resti possibili: o esce $0$ (sviluppo finito) o un resto si ripete e da lì in poi le cifre si ripetono. Viceversa, un periodo si trasforma in frazione: $0,\overline{34}=\frac{34}{99}$.

## Esempi

- $\frac34=0,75$ (finito).
- $\frac13=0,\overline3$.
- $\frac16=0,1\overline6$: il denominatore $6=2\cdot3$ contribuisce una parte non periodica e un periodo.

## Come si dimostra

Si usa il Lemma $0,\overline{b_0\cdots b_n}=\frac{B}{10^{n+1}-1}$ e il fatto che ogni $b$ divide $10^s(10^m-1)$ per opportuni $s,m$. Vedi [[2026-10-14 - Sviluppi decimali razionali e fattorizzazione dei denominatori#1. Sviluppi decimali e periodicità|la lezione del 14 ottobre]].

## Vedi anche

- [[Divisione euclidea]]
- [[Congruenza modulo n]]
- [[Numero primo]]
- [[Formula di Legendre]]
