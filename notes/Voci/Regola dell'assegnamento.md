---
title: Regola dell'assegnamento
type: voce
categoria: teorema
corsi:
- Fondamenti di Programmazione
introdotta_in: 2026-10-20 - Regole di inferenza per le triple di Hoare e invarianti
alias:
- assioma dell'assegnamento
- assegnamento
sintesi: Per avere una certa asserzione dopo un assegnamento basta che valga, prima, la stessa asserzione con l'espressione al posto della variabile.
---
La **regola dell'assegnamento** (o assioma dell'assegnamento) permette di ricavare, dalla postcondizione, la precondizione più debole di un comando `x := E`. Si usa *all'indietro*.

## Enunciato

$$
\{\mathrm{def}(E)\land P[E/x]\}\ x:=E\ \{P\}\qquad(\mathrm{ass})
$$

dove $P[E/x]$ è $P$ con $E$ al posto di $x$ e $\mathrm{def}(E)$ garantisce che $E$ si possa valutare senza errori (per esempio senza divisioni per zero). In forma comoda per verificare una tripla data:

$$
\frac{R\Rightarrow\mathrm{def}(E)\land P[E/x]}{\{R\}\ x:=E\ \{P\}}
$$

## Intuizione

Dopo l'assegnamento $x$ vale $E$ (calcolata nello stato di prima), quindi $P$ vale dopo se e solo se valeva prima la stessa $P$ con $E$ al posto di $x$. Verificare un assegnamento si riduce a dimostrare un'implicazione tra asserzioni.

## Esempi

- Per ottenere $x>y$ dopo `x := x+2`: la precondizione è $(x>y)[x+2/x]\equiv x+2>y$.
- $\{x=5\}\ x:=x+1\ \{x>2\}$: la sostituzione dà $x+1>2\equiv x>1$, e $x=5\Rightarrow x>1$.

## Come si dimostra

Segue dalla semantica $\mathcal C(x:=E,\sigma)=\sigma[\mathcal E(E,\sigma)/x]$ e dalla proprietà (P3), per cui $\sigma[\mathcal E(E,\sigma)/x]\models P$ se e solo se $\sigma\models P[E/x]$. Il congiunto $\mathrm{def}(E)$ assicura che la valutazione termini. Vedi [[2026-10-20 - Regole di inferenza per le triple di Hoare e invarianti#5. Assegnamento|la lezione del 20 ottobre]].

## Vedi anche

- [[Tripla di Hoare]]
- [[Precondizione e postcondizione]]
- [[Programma annotato]]
- [[Aggiornamento di un array]]
