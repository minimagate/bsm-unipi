---
title: Modulo di un numero complesso
type: voce
categoria: definizione
corsi:
- Geometria 1
introdotta_in: 2026-09-25 - Numeri complessi- operazioni, forma polare e radici
alias:
- norma di un numero complesso
- modulo complesso
sintesi: Il modulo di un numero complesso è la sua distanza dall'origine nel piano complesso.
---

Il **modulo** (o norma) di un numero complesso $z=a+ib$ è la distanza del punto $(a,b)$ dall'origine del piano complesso. Estende il valore assoluto dei numeri reali.

## Definizione

$$
|z|:=\sqrt{a^2+b^2}\in\mathbb{R}_{\geq 0}.
$$

Valgono $|z|=0\iff z=0$ e la relazione fondamentale con il coniugato:

$$
z\overline z=|z|^2.
$$

## Intuizione

È il teorema di Pitagora: $|z|$ è l'ipotenusa del triangolo rettangolo di cateti $|a|$ e $|b|$. In [[Forma polare|forma polare]] è proprio la distanza $\rho$. Nella formula non compare $i$, perché il modulo usa direttamente le coordinate reali.

## Esempi

- $|3+4i|=5$.
- $|-2|=\sqrt{(-2)^2+0^2}=2$: per un numero reale il modulo coincide con il [[Valore assoluto|valore assoluto]].
- $|1-i|^2=2$.

## Come si dimostra

Che $|z|=0$ implichi $z=0$ segue dal fatto che una somma di due quadrati reali è nulla solo se lo sono entrambi. La formula $z\overline z=|z|^2$ si ottiene sviluppando $(a+ib)(a-ib)$; vedi [[2026-09-25 - Numeri complessi- operazioni, forma polare e radici#11. Relazione tra modulo e coniugio|la relazione tra modulo e coniugio]].

## Vedi anche

- [[Numero complesso]]
- [[Coniugio complesso]]
- [[Forma polare]]
- [[Valore assoluto]]
