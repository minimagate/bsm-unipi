---
title: Teorema rango-nullità
type: voce
categoria: teorema
corsi:
- Geometria 1
introdotta_in: 2026-10-23 - Sistemi lineari, nucleo, immagine e rango
alias:
- teorema della dimensione
- formula rango-nucleo
- teorema del rango
sintesi: La dimensione dello spazio di partenza di un'applicazione lineare è la somma delle dimensioni del nucleo e dell'immagine.
---

Il **teorema rango-nullità** (o formula rango-nucleo) lega le dimensioni di nucleo e immagine di un'applicazione lineare: ciò che non finisce nel nucleo va a formare l'immagine.

## Enunciato

Sia $F:V\to V'$ un'applicazione lineare con $V$ di dimensione finita. Allora

$$
\dim V=\dim\ker(F)+\dim\operatorname{Im}(F).
$$

Per $F_A(x)=Ax$ con $A\in M_{m,n}(\mathbb K)$ diventa $\dim\ker(F_A)=n-\operatorname{rank}(A)$.

## Intuizione

La dimensione di $V$ si "spezza" in due parti: le direzioni che l'applicazione annulla (nucleo) e quelle che sopravvivono (immagine). Per i sistemi omogenei dice quanti parametri liberi hanno le soluzioni: $n$ meno il rango.

## Esempi

Per $A=\begin{pmatrix}1&2\\2&4\end{pmatrix}$ si ha $\dim\ker=1$ e $\operatorname{rank}=1$, e $1+1=2=\dim\mathbb R^2$.

Un sistema omogeneo di una sola equazione in $5$ incognite, non banale, ha rango $1$ e quindi soluzioni di dimensione $4$.

## Come si dimostra

Si prende una base $v_1,\dots,v_k$ del nucleo e la si completa a una base $v_1,\dots,v_n$ di $V$. Le immagini $F(v_{k+1}),\dots,F(v_n)$ generano l'immagine e sono linearmente indipendenti, quindi ne sono una base. La dimostrazione completa è [[2026-10-23 - Sistemi lineari, nucleo, immagine e rango#Teorema della dimensione: formula rango-nucleo|nella lezione del 23 ottobre]].

## Vedi anche

- [[Nucleo]]
- [[Rango]]
- [[Applicazione lineare]]
- [[Completamento a una base]]
