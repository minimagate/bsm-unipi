---
title: Dimensione di uno spazio vettoriale
type: voce
categoria: definizione
corsi:
- Geometria 1
introdotta_in: 2026-10-07 - Coordinate, basi e dimensione degli spazi vettoriali
alias:
- dimensione
- finitamente generato
- dim
sintesi: La dimensione di uno spazio vettoriale è il numero di elementi di una sua base, che è lo stesso per tutte le basi.
---

La **dimensione** di uno spazio vettoriale finitamente generato $V$ è il numero di elementi di una sua [[Base di uno spazio vettoriale|base]]. Si scrive $\dim_K V$ (o $\dim V$). Uno spazio è **finitamente generato** se ha un insieme finito di generatori.

## Definizione

$$
\dim_K(V)=n
$$

se e solo se ogni base di $V$ ha $n$ elementi. Che il numero sia lo stesso per tutte le basi è garantito dal [[Lemma di scambio]]. Ogni spazio finitamente generato ha una base finita (si eliminano i vettori ridondanti da un insieme di generatori).

## Intuizione

La dimensione è il numero di parametri indipendenti che servono per descrivere un vettore: le coordinate sono proprio $n$ numeri, e $V\cong K^n$. Alcune conseguenze: in dimensione $n$ un insieme indipendente ha al massimo $n$ vettori, un sistema di generatori ne ha almeno $n$, e un sottospazio $W\subseteq V$ ha $\dim W\leq\dim V$ con uguaglianza solo se $W=V$.

## Esempi

- $\dim_K(K^n)=n$.
- $\dim_K M_{m,n}(K)=mn$, in particolare $\dim M_2(K)=4$.
- $\mathbb{C}$ ha dimensione $1$ su $\mathbb{C}$ ma $2$ su $\mathbb{R}$: la dimensione dipende dal campo.
- $\mathbb{K}[x]$ ha dimensione infinita.

## Come si dimostra

Si usa il lemma di scambio per confrontare due basi: ciascuna ha al più tanti elementi quanto l'altra. Vedi [[2026-10-07 - Coordinate, basi e dimensione degli spazi vettoriali#Dimensione|la sezione Dimensione]] e [[2026-10-13 - Somma diretta e dimensione dei sottospazi#1. Dimensione e basi dei sottospazi|la dimensione dei sottospazi]].

## Vedi anche

- [[Base di uno spazio vettoriale]]
- [[Lemma di scambio]]
- [[Formula di Grassmann]]
- [[Teorema rango-nullità]]
