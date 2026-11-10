---
title: Lemma di scambio
type: voce
categoria: teorema
corsi:
- Geometria 1
introdotta_in: 2026-10-07 - Coordinate, basi e dimensione degli spazi vettoriali
alias:
- lemma dello scambio
- Steinitz
sintesi: Il lemma di scambio permette di sostituire un vettore di un insieme indipendente con un altro mantenendo indipendenza e span, e implica che tutte le basi hanno lo stesso numero di elementi.
---

Il **lemma di scambio** (o di Steinitz) è il risultato che permette di confrontare le basi: dice che si può sostituire un vettore di una famiglia indipendente con un altro senza perdere né l'indipendenza né lo span. La conseguenza principale è che tutte le basi di uno spazio finitamente generato hanno lo stesso numero di elementi.

## Enunciato

Siano $\{u_1,\dots,u_r\}$ linearmente indipendenti e $v=\alpha_1u_1+\cdots+\alpha_ru_r$ con $\alpha_1\neq 0$. Allora l'insieme $\{v,u_2,\dots,u_r\}$ è linearmente indipendente e ha lo stesso span di $\{u_1,\dots,u_r\}$.

Nella forma per basi: se $\mathcal B=(u_1,\dots,u_n)$ è una base e $w_1,\dots,w_m$ sono linearmente indipendenti, si possono scambiare i $w_i$ con vettori di $\mathcal B$ mantenendo sempre una base, e quindi $m\leq n$.

## Intuizione

Se $v$ dipende "davvero" da $u_1$ (cioè il suo coefficiente non è zero), possiamo usare $v$ al posto di $u_1$: $u_1$ si ricostruisce da $v$ e dagli altri. Ripetendo, si inseriscono i nuovi vettori uno alla volta, ma non se ne possono inserire più di $n$.

## Esempi

In $\mathbb{R}^2$ con $\{(1,0),(0,1)\}$ e $v=(2,3)=2(1,0)+3(0,1)$, sostituendo $(1,0)$ con $v$ si ottiene $\{(2,3),(0,1)\}$, ancora una base di $\mathbb{R}^2$.

Conseguenza: due basi $\mathcal B$ e $\mathcal C$ hanno $m\leq n$ e $n\leq m$, quindi $m=n$, ed è questo che rende ben definita la [[Dimensione di uno spazio vettoriale|dimensione]].

## Come si dimostra

Lo span coincide perché $u_1$ si ricava da $v$ e dagli altri; l'indipendenza segue sostituendo l'espressione di $v$ in una combinazione nulla e usando $\alpha_1\neq 0$. Vedi [[2026-10-07 - Coordinate, basi e dimensione degli spazi vettoriali#Lemma di scambio|il lemma di scambio nella lezione del 7 ottobre]].

## Vedi anche

- [[Base di uno spazio vettoriale]]
- [[Indipendenza lineare]]
- [[Dimensione di uno spazio vettoriale]]
