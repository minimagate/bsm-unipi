---
title: Indice di un sottogruppo
type: voce
categoria: definizione
corsi:
- Aritmetica
introdotta_in: 2026-11-09 - Classi laterali e teorema di Lagrange
alias:
- indice
sintesi: Il numero di classi laterali sinistre di un sottogruppo in un gruppo.
---

L'**indice** di un sottogruppo $H$ in $G$ dice in quante "fette" $H$ divide $G$.

## Definizione

Dato $H\leq G$, l'indice di $H$ in $G$ è il numero delle classi laterali sinistre di $H$ in $G$:

$$
[G:H].
$$

Se $G$ è finito, per il [[Teorema di Lagrange|teorema di Lagrange]]

$$
[G:H]=\frac{|G|}{|H|}.
$$

Se $G$ è infinito l'indice può essere infinito.

## Intuizione

Se $H$ ha 2 elementi e $G$ ne ha 6, ci stanno esattamente 3 fette da 2: l'indice è 3. È il "quoziente" tra le taglie di $G$ e $H$.

## Esempi

- Se $H\leq S_3$ ha ordine $2$, allora $[S_3:H]=6/2=3$: ci sono $3$ classi laterali sinistre, ciascuna con $2$ elementi.
- In $\mathbb Z$, il sottogruppo $n\mathbb Z$ ha indice $n$: le sue classi laterali sono le $n$ classi di congruenza modulo $n$.

## Vedi anche

- [[Classe laterale]]
- [[Teorema di Lagrange]]
- [[Sottogruppo]]
- [[Sottogruppo normale]]
