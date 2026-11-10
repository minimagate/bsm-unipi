---
title: Proprietà definitivamente vera
type: voce
categoria: notazione
corsi:
- Analisi 1
introdotta_in: 2026-10-06 - Successioni, limiti e teoremi di confronto
alias:
- definitivamente
- frequentemente
- vera definitivamente
sintesi: Una proprietà dipendente da n vale definitivamente se è vera da un certo indice in poi e frequentemente se è vera per infiniti indici.
---
Dire che una proprietà vale **definitivamente** (o *è vera definitivamente*) significa che è vera da un certo indice in poi; dire che vale **frequentemente** significa che è vera per infiniti indici.

## Definizione

Sia $P(n)$ un predicato sui numeri naturali.

- $P(n)$ vale **definitivamente** se $\exists n_0\in\mathbb{N}$ tale che $\forall n\ge n_0$ $P(n)$ è vera.
- $P(n)$ vale **frequentemente** se $\forall n_0\in\mathbb{N}$ $\exists n\ge n_0$ tale che $P(n)$ è vera.

## Intuizione

Per "definitivamente" non importa cosa succede nei primi indici: possono essercene finiti (anche tanti) in cui la proprietà è falsa. Per "frequentemente" gli indici in cui è vera non devono essere consecutivi, ma per quanto si vada avanti se ne trova sempre uno. È il linguaggio naturale per scrivere i [[Limite di una successione|limiti]]: "$a_n\ge M$ definitivamente".

## Esempi

- $n^2\ge 10^6$ vale definitivamente (da $n=1000$ in poi).
- $(-1)^n=1$ vale frequentemente ma non definitivamente.
- $\frac1{n-5}>0$ vale definitivamente (da $n=6$).

## Vedi anche

- [[Limite di una successione]]
- [[Successione]]
- [[Quantificatore]]
- [[Permanenza del segno]]
