---
title: Prodotto tra matrici
type: voce
categoria: definizione
corsi:
- Geometria 1
introdotta_in: 2026-10-14 - Basi, sottospazi e sistemi lineari
alias:
- prodotto righe per colonne
- prodotto matrice-vettore
- prodotto di matrici
sintesi: Si moltiplicano due matrici componendo righe della prima con colonne della seconda, a patto che le dimensioni interne coincidano.
---

Il **prodotto tra matrici** (o prodotto righe per colonne) è l'operazione che permette di scrivere un sistema lineare come $Ax=b$ e di rappresentare la composizione di applicazioni lineari.

## Definizione

Siano $A\in M_{m,n}(\mathbb K)$ e $B\in M_{n,p}(\mathbb K)$: il numero di colonne di $A$ deve coincidere con il numero di righe di $B$. Il prodotto $AB\in M_{m,p}(\mathbb K)$ ha come elemento nella posizione $(i,j)$

$$
(AB)_{ij}=\sum_{k=1}^{n}a_{ik}b_{kj}.
$$

In pratica si prende la riga $i$ di $A$, la colonna $j$ di $B$, si moltiplicano i termini corrispondenti e si somma. Il caso $p=1$ è il **prodotto matrice-vettore** $Av$, con $v$ vettore colonna.

## Intuizione

Le dimensioni si leggono come $(m\times n)(n\times p)=m\times p$: la dimensione interna "si consuma" e restano quelle esterne. Un modo utile di vedere $Ax$ è come combinazione lineare delle colonne di $A$ con coefficienti le componenti di $x$. Il prodotto è associativo e distributivo, ma **non commutativo**: in generale $AB\neq BA$.

## Esempi

Con $A=\begin{pmatrix}1&2\\0&1\end{pmatrix}$ e $x=\begin{pmatrix}3\\4\end{pmatrix}$ si ha $Ax=\begin{pmatrix}1\cdot3+2\cdot4\\0\cdot3+1\cdot4\end{pmatrix}=\begin{pmatrix}11\\4\end{pmatrix}$.

Il prodotto $AB$ con $A$ di tipo $2\times3$ e $B$ di tipo $3\times2$ è definito e di tipo $2\times2$, mentre $BA$ è di tipo $3\times3$: già le dimensioni sono diverse.

## Come si dimostra

Non c'è un teorema da dimostrare: è una definizione. La motivazione (il prodotto rappresenta la composizione di applicazioni lineari) è spiegata [[2026-11-04 - Applicazioni lineari e matrici associate#14. Matrice della composizione|nella lezione del 4 novembre]]. La definizione è introdotta [[2026-10-14 - Basi, sottospazi e sistemi lineari#12. Prodotto tra matrici|nella lezione del 14 ottobre]].

## Vedi anche

- [[Matrice]]
- [[Sistema lineare]]
- [[Combinazione lineare]]
- [[Matrice associata a un'applicazione lineare]]
