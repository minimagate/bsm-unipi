---
title: Coordinate rispetto a una base
type: voce
categoria: definizione
corsi:
- Geometria 1
introdotta_in: 2026-10-07 - Coordinate, basi e dimensione degli spazi vettoriali
alias:
- coordinate
- base ordinata
- mappa delle coordinate
sintesi: Le coordinate di un vettore rispetto a una base sono i coefficienti dell'unica combinazione lineare dei vettori della base che lo rappresenta.
---

Fissata una [[Base di uno spazio vettoriale|base]] ordinata $\mathcal B=(v_1,\dots,v_n)$ di $V$, ogni vettore $v\in V$ si scrive in modo unico come combinazione lineare dei vettori di $\mathcal B$; i coefficienti sono le **coordinate** di $v$ rispetto a $\mathcal B$.

## Definizione

Se $v=x_1v_1+\cdots+x_nv_n$, il **vettore delle coordinate** è

$$
[v]_{\mathcal B}
=
\begin{pmatrix}
x_1\\
\vdots\\
x_n
\end{pmatrix}\in K^n.
$$

La **mappa delle coordinate** è $\Phi_{\mathcal B}:V\to K^n$, $v\mapsto[v]_{\mathcal B}$. È lineare e biettiva, quindi un [[Isomorfismo|isomorfismo]]: $V\cong K^n$. Se la base è infinita, le coordinate sono funzioni $\mathcal B\to K$ a supporto finito.

## Intuizione

Le coordinate non appartengono al vettore in assoluto: dipendono dalla base. Lo stesso vettore ha coordinate diverse in basi diverse, e perfino l'ordine dei vettori della base conta. Una volta scelta la base, un vettore astratto diventa una colonna di numeri e le operazioni diventano quelle di [[Spazio K^n]].

## Esempi

- In $\mathbb{R}^2$ con $\mathcal B=(e_1,e_2)$ e $\mathcal B'=(e_2,e_1)$, il vettore $v=xe_1+ye_2$ ha $[v]_{\mathcal B}=(x,y)^T$ e $[v]_{\mathcal B'}=(y,x)^T$.
- Rispetto alla base canonica di $K^n$ le coordinate coincidono con le entrate del vettore.
- In $M_{m,n}(K)$ la coordinata di $A$ lungo $E_{ij}$ è l'elemento $a_{ij}$.

## Come si dimostra

Somma e prodotto per scalare si trasportano sulle coordinate, e iniettività e suriettività seguono dall'unicità dello sviluppo: vedi [[2026-10-07 - Coordinate, basi e dimensione degli spazi vettoriali#La mappa delle coordinate è un isomorfismo|la mappa delle coordinate è un isomorfismo]].

## Vedi anche

- [[Base di uno spazio vettoriale]]
- [[Isomorfismo]]
- [[Dimensione di uno spazio vettoriale]]
- [[Matrice associata a un'applicazione lineare]]
