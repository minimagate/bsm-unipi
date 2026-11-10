---
title: Matrice invertibile
type: voce
categoria: definizione
corsi:
- Geometria 1
introdotta_in: 2026-10-27 - Rango, sistemi lineari e matrici elementari
alias:
- matrici invertibili
- gruppo lineare generale
- GL_n
sintesi: Matrice quadrata che ammette una matrice inversa; le matrici invertibili di un dato ordine formano un gruppo rispetto al prodotto.
---

Una **matrice invertibile** è una matrice quadrata $P$ per cui esiste una matrice $Q$ che "annulla" l'effetto di $P$ nel prodotto. Le matrici invertibili di ordine $m$ formano un gruppo, il **gruppo lineare generale** $GL_m(\mathbb K)$.

## Definizione

Una matrice $P\in M_m(\mathbb K)$ è invertibile se esiste $Q\in M_m(\mathbb K)$ tale che

$$
PQ=QP=I_m.
$$

Si scrive $Q=P^{-1}$. Se $P$ e $Q$ sono invertibili, anche $PQ$ lo è e $(PQ)^{-1}=Q^{-1}P^{-1}$. Per $m\geq 2$ il gruppo $GL_m(\mathbb K)$ non è commutativo; $GL_1(\mathbb K)=\mathbb K^\times$.

## Intuizione

Una matrice invertibile è una trasformazione che si può annullare: non perde informazione. Equivale a dire che ha rango $m$, cioè che $x\mapsto Px$ è biettiva. Si lega alle operazioni di riga: ogni matrice invertibile è prodotto di matrici elementari, cioè si ottiene dall'identità con operazioni di riga.

## Esempi

La matrice $\begin{pmatrix}0&1\\1&0\end{pmatrix}$ è invertibile e coincide con la propria inversa (scambio di righe).

La matrice $\begin{pmatrix}1&2\\2&4\end{pmatrix}$ non è invertibile: ha rango $1<2$.

## Come si dimostra

Se $P$ è invertibile, da $Px=0$ segue $x=P^{-1}Px=0$, quindi il nucleo è banale e per rango-nullità il rango è $m$. Riducendo $P$ alla forma ridotta si ottiene $I_m$, da cui $P=E_1^{-1}\cdots E_r^{-1}$. I dettagli sono [[2026-10-27 - Rango, sistemi lineari e matrici elementari#12. Ogni matrice invertibile è prodotto di matrici elementari|nella lezione del 27 ottobre]].

## Vedi anche

- [[Matrice elementare]]
- [[Gruppo]]
- [[Rango]]
- [[Funzione inversa]]
