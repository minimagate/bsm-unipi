---
title: Base di uno spazio vettoriale
type: voce
categoria: definizione
corsi:
- Geometria 1
introdotta_in: 2026-10-02 - Span, indipendenza lineare e basi vettoriali
alias:
- base
- basi
- base canonica
sintesi: Una base di uno spazio vettoriale è un insieme di vettori linearmente indipendenti che generano lo spazio.
---

Una **base** di uno [[Spazio vettoriale|spazio vettoriale]] $V$ è un insieme di vettori che genera $V$ ed è linearmente indipendente. Permette di descrivere ogni vettore in modo unico tramite le sue [[Coordinate rispetto a una base|coordinate]].

## Definizione

$B\subseteq V$ è una base se

1. $\operatorname{span}(B)=V$ ([[Sottospazio generato]]);
2. $B$ è [[Indipendenza lineare|linearmente indipendente]].

La generazione garantisce l'*esistenza* dello sviluppo di ogni vettore, l'indipendenza ne garantisce l'*unicità*. Equivalentemente, una base è un insieme di vettori indipendenti massimale, oppure un insieme di generatori minimale.

## Intuizione

È un sistema di riferimento senza ridondanze: abbastanza vettori per raggiungere tutto, nessuno in più. Lo stesso spazio ha molte basi; ciò che non cambia è il numero di elementi (la [[Dimensione di uno spazio vettoriale|dimensione]]).

## Esempi

- La **base canonica** di $\mathbb{K}^n$: $e_1,\dots,e_n$, dove $e_i$ ha $1$ al posto $i$ e zeri altrove.
- In $\mathbb{R}^2$ anche $(1,1)$ e $(1,-1)$ sono una base.
- $\{1,i\}$ è una base di $\mathbb{C}$ su $\mathbb{R}$.
- I monomi $1,x,x^2,\dots$ sono una base (infinita) di $\mathbb{K}[x]$.

## Come si dimostra

Per verificare che un insieme sia una base si dimostrano le due condizioni separatamente. Per la base canonica: [[2026-10-02 - Span, indipendenza lineare e basi vettoriali#14. La base canonica di $\mathbb{K}^n$|la base canonica di K^n]].

## Vedi anche

- [[Coordinate rispetto a una base]]
- [[Dimensione di uno spazio vettoriale]]
- [[Lemma di scambio]]
- [[Spazio K^n]]
