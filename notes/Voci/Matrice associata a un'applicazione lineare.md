---
title: Matrice associata a un'applicazione lineare
type: voce
categoria: definizione
corsi:
- Geometria 1
introdotta_in: 2026-11-04 - Applicazioni lineari e matrici associate
alias:
- matrice associata
- matrice di un'applicazione lineare
sintesi: Matrice le cui colonne sono le coordinate delle immagini dei vettori della base di partenza rispetto alla base di arrivo.
---

La **matrice associata** a un'applicazione lineare, rispetto a due basi fissate, è la matrice che rappresenta l'applicazione in coordinate. Con le basi scelte, applicare $F$ equivale a moltiplicare per questa matrice.

## Definizione

Siano $F:V\to W$ lineare, $\mathcal B=(v_1,\dots,v_n)$ una base di $V$ e $\mathcal B'=(w_1,\dots,w_m)$ una base di $W$. La matrice associata è

$$
M_{\mathcal B,\mathcal B'}(F)=\Big([F(v_1)]_{\mathcal B'}\ \cdots\ [F(v_n)]_{\mathcal B'}\Big)\in M_{m\times n}(\mathbb K),
$$

cioè la $j$-esima colonna contiene le coordinate di $F(v_j)$ rispetto a $\mathcal B'$. Vale la formula fondamentale

$$
[F(v)]_{\mathcal B'}=M_{\mathcal B,\mathcal B'}(F)\,[v]_{\mathcal B}.
$$

## Intuizione

Le coordinate trasformano $V$ in $\mathbb K^n$ e $W$ in $\mathbb K^m$; in questi spazi $F$ diventa $x\mapsto Ax$. La matrice dipende dalle basi: cambiando basi cambia la matrice. Nucleo, immagine e rango di $F$ si calcolano da quelli di $A$, e la matrice della composizione $G\circ F$ è il prodotto $BA$.

## Esempi

Per $F(x,y)=(x+y,2y)$ con la base canonica in partenza e in arrivo: $F(e_1)=(1,0)$, $F(e_2)=(1,2)$, quindi $M(F)=\begin{pmatrix}1&1\\0&2\end{pmatrix}$.

Per $F(X)=AX-XA$ su $M_{2\times2}(\mathbb R)$ con $A=\begin{pmatrix}0&1\\1&0\end{pmatrix}$ e la base canonica $(E_{11},E_{12},E_{21},E_{22})$ si ottiene una matrice $4\times4$ di rango $2$.

## Come si dimostra

La formula fondamentale segue dalla linearità: $F(v)=\sum x_jF(v_j)$, da cui $[F(v)]_{\mathcal B'}=\sum x_j[F(v_j)]_{\mathcal B'}$. Si veda [[2026-11-04 - Applicazioni lineari e matrici associate#4. Formula fondamentale delle coordinate|la lezione del 4 novembre]]; la definizione è [[2026-11-04 - Applicazioni lineari e matrici associate#3. Matrice associata a un’applicazione lineare|nel §3]].

## Vedi anche

- [[Applicazione lineare]]
- [[Coordinate rispetto a una base]]
- [[Prodotto tra matrici]]
- [[Isomorfismo]]
