---
title: Matrice elementare
type: voce
categoria: oggetto
corsi:
- Geometria 1
introdotta_in: 2026-10-27 - Rango, sistemi lineari e matrici elementari
alias:
- matrici elementari
sintesi: Matrice quadrata invertibile che, moltiplicata a sinistra, realizza una singola operazione elementare di riga.
---

Una **matrice elementare** è una matrice quadrata invertibile che, moltiplicata a sinistra per $A$, esegue una singola operazione elementare di riga su $A$. È il modo di trasformare l'eliminazione di Gauss in un prodotto di matrici.

## Definizione

Per $A\in M_{m,n}(\mathbb K)$ le matrici elementari di ordine $m$ sono di tre tipi:

- $P_{ij}$: la matrice identità con le righe $i$ e $j$ scambiate; $P_{ij}A$ scambia le righe $i$ e $j$ di $A$;
- $D_i(\lambda)=\operatorname{diag}(1,\dots,\lambda,\dots,1)$ con $\lambda\neq 0$ in posizione $i$; moltiplica la riga $i$ per $\lambda$;
- $E_{ij}(\lambda)=I_m+\lambda E_{ij}$ con $i\neq j$; sostituisce $R_i$ con $R_i+\lambda R_j$.

## Intuizione

Moltiplicare a sinistra agisce sulle righe, a destra sulle colonne. Ogni operazione di riga è reversibile, e infatti le matrici elementari sono invertibili con inversa ancora elementare: $P_{ij}^{-1}=P_{ij}$, $D_i(\lambda)^{-1}=D_i(\lambda^{-1})$, $E_{ij}(\lambda)^{-1}=E_{ij}(-\lambda)$. Una successione di operazioni che porta $A$ in $S$ si scrive $S=E_r\cdots E_1A$.

## Esempi

Con $m=2$, $E_{21}(-2)=\begin{pmatrix}1&0\\-2&1\end{pmatrix}$ e $E_{21}(-2)\begin{pmatrix}1&2\\2&5\end{pmatrix}=\begin{pmatrix}1&2\\0&1\end{pmatrix}$: la seconda riga è diventata $R_2-2R_1$.

Attenzione: nella lezione del 14 ottobre $E_{ij}$ indica anche la matrice con un solo $1$ in posizione $(i,j)$, che fa parte della base di $M_{m,n}$ e non è invertibile.

## Come si dimostra

L'azione di ciascun tipo di matrice sulle righe e la loro invertibilità sono verificate [[2026-10-27 - Rango, sistemi lineari e matrici elementari#9. Matrici elementari e operazioni di riga|nella lezione del 27 ottobre]]. Ne segue che ogni matrice invertibile è prodotto di matrici elementari.

## Vedi anche

- [[Operazione elementare di riga]]
- [[Matrice invertibile]]
- [[Algoritmo di eliminazione di Gauss]]
- [[Prodotto tra matrici]]
