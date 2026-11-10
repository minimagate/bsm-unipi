---
title: Coniugio complesso
type: voce
categoria: definizione
corsi:
- Geometria 1
introdotta_in: 2026-09-25 - Numeri complessi- operazioni, forma polare e radici
alias:
- coniugato
- numero complesso coniugato
- coniugato complesso
sintesi: Il coniugato di un numero complesso ha la stessa parte reale e parte immaginaria opposta.
---

Il **coniugato** del numero complesso $z=a+ib$ è $\overline z:=a-ib$. Geometricamente, il coniugio è la riflessione rispetto all'asse reale del piano complesso.

## Definizione

$$
\overline{a+ib}=a-ib.
$$

Il coniugio lascia invariata la parte reale e cambia segno alla parte immaginaria. Valgono, per ogni $z,w\in\mathbb{C}$:

$$
\overline{z+w}=\overline z+\overline w,
\qquad
\overline{zw}=\overline z\,\overline w,
\qquad
\overline{\overline z}=z.
$$

Inoltre $z=\overline z$ se e solo se $z\in\mathbb{R}$, e $z\overline z=|z|^2$.

## Intuizione

Il coniugio rispetta somma e prodotto, quindi è una "simmetria" dei complessi che lascia fissi esattamente i reali. È utile soprattutto per due cose: eliminare la parte immaginaria dai denominatori e capire le radici dei polinomi con coefficienti reali.

## Esempi

- $\overline{2-3i}=2+3i$.
- $\dfrac{1}{a+ib}=\dfrac{a-ib}{a^2+b^2}$.
- Se $P$ ha coefficienti reali e $P(z_0)=0$, allora $P(\overline{z_0})=0$: le radici non reali compaiono a coppie coniugate.

## Come si dimostra

Per la somma basta scrivere $z=a+ib$, $w=c+id$ e confrontare i due membri; vedi [[2026-09-25 - Numeri complessi- operazioni, forma polare e radici#10. Proprietà del coniugio|le proprietà del coniugio]]. L'uso sulle radici è nella lezione del 1 ottobre ([[2026-10-01 - Fattorizzazione dei polinomi e radici complesse#9. Coniugio delle radici di un polinomio reale|coniugio delle radici di un polinomio reale]]).

## Vedi anche

- [[Numero complesso]]
- [[Modulo di un numero complesso]]
- [[Radice di un polinomio]]
