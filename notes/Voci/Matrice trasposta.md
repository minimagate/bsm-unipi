---
title: Matrice trasposta
type: voce
categoria: definizione
corsi:
- Geometria 1
introdotta_in: 2026-10-13 - Somma diretta e dimensione dei sottospazi
alias:
- trasposta
- matrice simmetrica
- matrice antisimmetrica
- matrici simmetriche
sintesi: La trasposta di una matrice si ottiene scambiando righe e colonne; una matrice quadrata è simmetrica se coincide con la propria trasposta e antisimmetrica se coincide con l'opposto.
---

La **trasposta** di una [[Matrice|matrice]] $M$ si ottiene scambiando righe e colonne. Una matrice quadrata si dice **simmetrica** se coincide con la sua trasposta, **antisimmetrica** se coincide con la trasposta cambiata di segno.

## Definizione

Se $M=(a_{ij})$ è $m\times n$, la trasposta $M^T$ è la matrice $n\times m$ definita da $(M^T)_{ij}=a_{ji}$. Per $A$ quadrata:

$$
A\text{ simmetrica}\iff A=A^T,
\qquad
A\text{ antisimmetrica}\iff A=-A^T.
$$

Nel caso reale una matrice antisimmetrica ha diagonale nulla, perché $a_{ii}=-a_{ii}$ implica $2a_{ii}=0$.

## Intuizione

La simmetria è rispetto alla diagonale principale: gli elementi simmetrici sono uguali (simmetrica) oppure opposti (antisimmetrica). Entrambi gli insiemi sono sottospazi di $M_n(\mathbb{R})$, e l'unica matrice che è sia simmetrica sia antisimmetrica è quella nulla.

## Esempi

$$
M=\begin{pmatrix}a&b\\c&d\end{pmatrix}
\ \Longrightarrow\ 
M^T=\begin{pmatrix}a&c\\b&d\end{pmatrix}.
$$

Una matrice $2\times 2$ simmetrica è $\begin{pmatrix}a&b\\b&d\end{pmatrix}$, una antisimmetrica $\begin{pmatrix}0&b\\-b&0\end{pmatrix}$.

Ogni matrice quadrata reale $M$ si scrive come $M=S+A$ con $S=\frac12(M+M^T)$ simmetrica e $A=\frac12(M-M^T)$ antisimmetrica, e si ha $M_n(\mathbb{R})=\mathcal S_n\oplus\mathcal A_n$ (vedi [[Somma diretta]]).

## Come si dimostra

Si verifica che $S^T=S$ e $A^T=-A$ usando $(M^T)^T=M$ e che l'intersezione dei due sottospazi è nulla: vedi [[2026-10-13 - Somma diretta e dimensione dei sottospazi#11.5. Decomposizione canonica|la decomposizione canonica]].

## Vedi anche

- [[Matrice]]
- [[Somma diretta]]
- [[Sottospazio vettoriale]]
- [[Prodotto tra matrici]]
