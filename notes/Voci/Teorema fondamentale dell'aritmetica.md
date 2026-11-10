---
title: Teorema fondamentale dell'aritmetica
type: voce
categoria: teorema
corsi:
- Aritmetica
introdotta_in: 2026-09-23 - Numeri naturali, induzione e fattorizzazione
alias:
- fattorizzazione unica
- fattorizzazione in primi
sintesi: Ogni intero maggiore di uno si scrive come prodotto di numeri primi in modo unico, a meno dell'ordine dei fattori.
---

Il **teorema fondamentale dell'aritmetica** afferma che ogni numero naturale $n\ge 2$ si fattorizza in numeri primi, e che questa fattorizzazione è unica a meno dell'ordine.

## Enunciato

Per ogni $n\ge 2$ esistono primi $p_1,\ldots,p_r$ con

$$n=p_1p_2\cdots p_r,$$

e se anche $n=q_1\cdots q_s$ con $q_j$ primi, allora $r=s$ e i $q_j$ coincidono con i $p_i$ a meno di un riordinamento. Con le potenze: $n=p_1^{\alpha_1}\cdots p_k^{\alpha_k}$ con esponenti univocamente determinati.

## Intuizione

Ogni numero ha un'"impronta digitale" fatta dai suoi fattori primi, e non ce n'è un'altra. Per esempio $2\cdot 5=5\cdot 2$ non sono due fattorizzazioni diverse. Dall'unicità si ricavano [[Massimo comun divisore]], [[Minimo comune multiplo]] e il conteggio dei divisori.

## Esempi

- $100=2^2\cdot 5^2$.
- $2000=2^4\cdot 5^3$ ha $(4+1)(3+1)=20$ divisori positivi.

## Come si dimostra

L'*esistenza* si dimostra per [[Induzione forte]] ([[2026-09-23 - Numeri naturali, induzione e fattorizzazione#10. Dimostrazione dell’esistenza della fattorizzazione mediante induzione forte|lezione del 23 settembre]]): se $n$ è composto, $n=ab$ con $a,b<n$ fattorizzabili. L'*unicità* usa il [[Lemma di Euclide]], per induzione sulla lunghezza ([[2026-10-08 - Fattorizzazione unica, congruenze e sistemi modulari#2. Unicità della fattorizzazione in primi|lezione dell'8 ottobre]]).

## Vedi anche

- [[Numero primo]]
- [[Lemma di Euclide]]
- [[Induzione forte]]
- [[Massimo comun divisore]]
