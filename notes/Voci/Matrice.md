---
title: Matrice
type: voce
categoria: oggetto
corsi:
- Geometria 1
introdotta_in: 2026-10-06 - Sottospazi, combinazioni lineari e basi
alias:
- matrici
- spazio delle matrici
sintesi: Una matrice è una tabella rettangolare di elementi di un campo; le matrici m per n formano uno spazio vettoriale.
---

Una **matrice** $m\times n$ a coefficienti in un campo $K$ è una tabella rettangolare di elementi di $K$ con $m$ righe e $n$ colonne. L'insieme di tutte le matrici $m\times n$ si indica con $M_{m,n}(K)$ (o $M_n(K)$ se $m=n$, matrici quadrate).

## Definizione

$$
A=
\begin{pmatrix}
a_{11} & \cdots & a_{1n}\\
\vdots & \ddots & \vdots\\
a_{m1} & \cdots & a_{mn}
\end{pmatrix},
\qquad a_{ij}\in K.
$$

Il primo indice è la riga, il secondo la colonna. Somma e prodotto per scalare sono componente per componente:

$$
(A+B)_{ij}=a_{ij}+b_{ij},
\qquad
(\lambda A)_{ij}=\lambda a_{ij}.
$$

La somma richiede matrici dello stesso tipo. Il vettore nullo è la matrice con tutti gli elementi nulli.

## Intuizione

Come lista di numeri, solo disposti in una tabella con due indici: $M_{m,n}(K)$ ha la stessa struttura di $K^{mn}$. Il [[Prodotto tra matrici|prodotto tra matrici]] è un'operazione diversa e non serve per dire che $M_{m,n}(K)$ è uno [[Spazio vettoriale|spazio vettoriale]].

## Esempi

- Una base canonica è data dalle matrici $E_{ij}$, con un $1$ nella posizione $(i,j)$ e zeri altrove; quindi $\dim M_{m,n}(K)=mn$ e $\dim M_2(K)=4$.
- Ogni matrice è $A=\sum a_{ij}E_{ij}$.
- Le matrici simmetriche e antisimmetriche sono due sottospazi di $M_n(\mathbb{R})$ (vedi [[Matrice trasposta]]).

## Come si dimostra

Che $M_{m,n}(K)$ sia uno spazio vettoriale segue dalle proprietà di $K$; la base canonica è in [[2026-10-07 - Coordinate, basi e dimensione degli spazi vettoriali#La base canonica di $M_{m,n}(K)$|la lezione del 7 ottobre]], l'introduzione in [[2026-10-06 - Sottospazi, combinazioni lineari e basi#2. Matrici come spazio vettoriale|quella del 6 ottobre]].

## Vedi anche

- [[Spazio vettoriale]]
- [[Matrice trasposta]]
- [[Prodotto tra matrici]]
- [[Base di uno spazio vettoriale]]
