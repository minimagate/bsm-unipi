---
title: Numero complesso
type: voce
categoria: oggetto
corsi:
- Aritmetica
- Geometria 1
introdotta_in: 2026-09-25 - Numeri complessi- operazioni, forma polare e radici
alias:
- numeri complessi
- piano complesso
sintesi: Un numero complesso si scrive come a più i volte b, con a e b reali, e si rappresenta come un punto del piano.
---

Un **numero complesso** è un'espressione $z=a+ib$ con $a,b\in\mathbb{R}$, dove $i$ è l'unità immaginaria, con $i^2=-1$. L'insieme dei numeri complessi è $\mathbb{C}$, ed è un [[Campo|campo]] che contiene $\mathbb{R}$.

## Definizione

$$
\mathbb{C}=\{a+ib\mid a,b\in\mathbb{R}\}.
$$

Il numero $a$ è la parte reale $\operatorname{Re}(z)$, $b$ è la parte immaginaria $\operatorname{Im}(z)$. Le operazioni sono

$$
(a+ib)+(c+id)=(a+c)+i(b+d),
\qquad
(a+ib)(c+id)=(ac-bd)+i(ad+bc).
$$

Ogni numero complesso non nullo ha inverso $z^{-1}=\dfrac{\overline z}{|z|^2}$ (vedi [[Coniugio complesso]] e [[Modulo di un numero complesso]]).

## Intuizione

$\mathbb{C}$ si identifica con $\mathbb{R}^2$: il numero $a+ib$ è il punto $(a,b)$ del **piano complesso**, con i reali sull'asse orizzontale. La somma è quella dei vettori (regola del parallelogramma); il prodotto, in [[Forma polare|forma polare]], moltiplica i moduli e somma gli argomenti, quindi è una rotazione più una dilatazione.

## Esempi

- $(2+i)+(3-2i)=5-i$.
- $(2+i)(3-2i)=8-i$.
- $\dfrac{3-2i}{1-i}=\dfrac52+\dfrac12 i$.

## Come si dimostra

Che $\mathbb{C}$ sia un campo si verifica assioma per assioma a partire dalle proprietà di $\mathbb{R}$; l'inverso si costruisce con il coniugato. Vedi [[2026-09-25 - Numeri complessi- operazioni, forma polare e radici#6. Verifica delle proprietà di campo|la verifica delle proprietà di campo]] e [[2026-09-25 - Numeri complessi- operazioni, forma polare e radici#12. Inverso moltiplicativo|l'inverso moltiplicativo]].

## Vedi anche

- [[Modulo di un numero complesso]]
- [[Coniugio complesso]]
- [[Forma polare]]
- [[Teorema fondamentale dell'algebra]]
