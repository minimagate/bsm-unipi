---
title: Teorema di Lagrange
type: voce
categoria: teorema
corsi:
- Aritmetica
introdotta_in: 2026-11-09 - Classi laterali e teorema di Lagrange
alias:
- Lagrange
sintesi: In un gruppo finito l'ordine di ogni sottogruppo divide l'ordine del gruppo.
---

Il **teorema di Lagrange** dice che un sottogruppo non può avere un numero di elementi qualsiasi: la sua taglia deve dividere quella del gruppo.

## Enunciato

Sia $G$ un gruppo finito e $H\leq G$ un [[Sottogruppo|sottogruppo]]. Allora

$$
|H|\ \text{divide}\ |G|,\qquad |G|=[G:H]\cdot|H|.
$$

Conseguenze: l'ordine di ogni elemento divide $|G|$; vale $x^{|G|}=e$ per ogni $x\in G$; ogni gruppo di ordine primo è ciclico.

## Intuizione

Le [[Classe laterale|classi laterali]] di $H$ tagliano $G$ in fette disgiunte, tutte con $|H|$ elementi. Contando gli elementi di $G$ fetta per fetta si ottiene un multiplo di $|H|$.

## Esempi

- In $S_3$ ($6$ elementi) non esistono sottogruppi di ordine $4$ o $5$; quelli di ordine $2$ hanno indice $3$.
- Un gruppo di ordine $7$ è ciclico: ogni $x\neq e$ ha ordine che divide $7$ e non è $1$, quindi è $7$ e $\langle x\rangle=G$.
- Applicato a $(\mathbb Z/m\mathbb Z)^\times$ (ordine $\varphi(m)$) dà il [[Piccolo teorema di Fermat|teorema di Eulero e di Fermat]].

## Come si dimostra

Si scrive $G=\bigsqcup_{x\in R}xH$ con $R$ un insieme di rappresentanti, e si usa $|xH|=|H|$ per ottenere $|G|=|R|\cdot|H|$. Si veda la [[2026-11-09 - Classi laterali e teorema di Lagrange#7. Il teorema di Lagrange|sezione sul teorema di Lagrange]] nella lezione del 9 novembre.

## Vedi anche

- [[Classe laterale]]
- [[Indice di un sottogruppo]]
- [[Ordine di un elemento]]
- [[Piccolo teorema di Fermat]]
