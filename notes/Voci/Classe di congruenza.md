---
title: Classe di congruenza
type: voce
categoria: oggetto
corsi:
- Aritmetica
introdotta_in: 2026-10-08 - Fattorizzazione unica, congruenze e sistemi modulari
alias:
- classi di congruenza
- classe di resto
- classi di resto
- Z/nZ
sintesi: La classe di congruenza di un intero modulo n è l'insieme di tutti gli interi congrui a esso modulo n.
---

La **classe di congruenza** di $a$ modulo $n$ è l'insieme degli interi congrui ad $a$ modulo $n$. L'insieme delle classi si indica con $\mathbb{Z}/n\mathbb{Z}$.

## Definizione

$$[a]_n=\{b\in\mathbb{Z}:b\equiv a\pmod n\}=\{a+kn:k\in\mathbb{Z}\}.$$

È una progressione aritmetica di ragione $n$. Ogni intero sta in una e una sola delle $n$ classi $[0]_n,[1]_n,\ldots,[n-1]_n$, quindi le classi si rappresentano con i resti $0,1,\ldots,n-1$. Scrivere $x\equiv a\pmod n$ equivale a $x\in[a]_n$.

## Intuizione

Una classe è "tutti i numeri che a quell'ora segnano lo stesso". Per lavorare con le congruenze non servono i singoli numeri, ma le classi: $7$ e $1$ rappresentano la stessa classe modulo $3$.

## Esempi

Modulo $5$: $[2]_5=\{\ldots,-8,-3,2,7,12,\ldots\}$. Modulo $6$ ci sono sei classi; $[0]_6$ contiene tutti i multipli di $6$.

## Come si dimostra

Vedi [[2026-10-08 - Fattorizzazione unica, congruenze e sistemi modulari#5. Classi di congruenza|la lezione dell'8 ottobre]].

## Vedi anche

- [[Congruenza modulo n]]
- [[Relazione di equivalenza]]
- [[Inverso modulo n]]
- [[Teorema cinese del resto]]
