---
title: Sistema lineare
type: voce
categoria: oggetto
corsi:
- Geometria 1
introdotta_in: 2026-10-14 - Basi, sottospazi e sistemi lineari
alias:
- sistemi lineari
- sistema omogeneo
- sistema omogeneo associato
sintesi: Insieme di equazioni di primo grado nelle stesse incognite, che si scrive in modo compatto come un prodotto tra una matrice e un vettore.
---

Un **sistema lineare** è un insieme di equazioni di primo grado nelle stesse incognite. Si scrive in forma compatta come $Ax=b$, dove $A$ è la matrice dei coefficienti.

## Definizione

Un sistema di $m$ equazioni in $n$ incognite su un campo $\mathbb K$ ha la forma

$$
\begin{cases}
a_{11}x_1+\cdots+a_{1n}x_n=b_1\\
\vdots\\
a_{m1}x_1+\cdots+a_{mn}x_n=b_m.
\end{cases}
$$

Con $A=(a_{ij})\in M_{m,n}(\mathbb K)$, $x\in\mathbb K^n$ e $b\in\mathbb K^m$ diventa $Ax=b$. Se $b=0$ il sistema è **omogeneo**. La matrice $(A\mid b)$ si chiama matrice completa.

## Intuizione

Risolvere $Ax=b$ vuol dire cercare i coefficienti con cui scrivere $b$ come combinazione lineare delle colonne di $A$. Le soluzioni di un sistema omogeneo formano un sottospazio (il nucleo di $A$); quelle di un sistema compatibile non omogeneo sono una soluzione particolare più una qualunque soluzione dell'omogeneo associato, cioè un traslato di quel sottospazio.

## Esempi

Il sistema $x+2y=3$, $4x-y=1$ si scrive $Ax=b$ con $A=\begin{pmatrix}1&2\\4&-1\end{pmatrix}$ e $b=\begin{pmatrix}3\\1\end{pmatrix}$.

Il sistema omogeneo $x_1+2x_2-x_3=0$ in $\mathbb R^3$ ha come soluzioni un piano passante per l'origine.

## Come si dimostra

La scrittura matriciale si ricava dal prodotto matrice-vettore, come spiegato [[2026-10-14 - Basi, sottospazi e sistemi lineari#13. Sistemi lineari in forma matriciale|nella lezione del 14 ottobre]]. Il metodo pratico di risoluzione è l'eliminazione di Gauss.

## Vedi anche

- [[Prodotto tra matrici]]
- [[Algoritmo di eliminazione di Gauss]]
- [[Teorema di Rouché-Capelli]]
- [[Nucleo]]
