---
title: Omomorfismo
type: voce
categoria: definizione
corsi:
- Aritmetica
introdotta_in: 2026-10-22 - Omomorfismi tra anelli e teorema cinese
alias:
- omomorfismi
- omomorfismo di gruppi
- omomorfismo di anelli
sintesi: Una funzione tra due strutture algebriche che conserva le operazioni.
---

Un **omomorfismo** è una [[Funzione|funzione]] tra due strutture algebriche (gruppi, anelli, spazi vettoriali) che rispetta le operazioni: calcolare prima e poi trasportare, oppure trasportare e poi calcolare, dà lo stesso risultato.

## Definizione

- Tra [[Gruppo|gruppi]] $(G,\cdot)$ e $(H,*)$: $f(x\cdot y)=f(x)*f(y)$ per ogni $x,y\in G$.
- Tra [[Anello|anelli]]: $f(a_1+a_2)=f(a_1)+f(a_2)$ e $f(a_1a_2)=f(a_1)f(a_2)$; con l'identità si richiede anche $f(1_A)=1_B$.

Un omomorfismo biettivo è un [[Isomorfismo|isomorfismo]]. Un omomorfismo manda l'identità nell'identità, $f(x^{-1})=f(x)^{-1}$ e $f(x^n)=f(x)^n$.

## Intuizione

Un omomorfismo è una "traduzione fedele" dalla struttura di partenza a quella di arrivo: può perdere informazioni (se non è iniettivo), ma non rompe le regole del gioco. Per gli spazi vettoriali gli omomorfismi sono le applicazioni lineari.

## Esempi

- La riduzione $\mathbb Z\to\mathbb Z/n\mathbb Z$, $a\mapsto[a]_n$, è un omomorfismo di anelli.
- $\mathbb Z/mn\mathbb Z\to\mathbb Z/m\mathbb Z\times\mathbb Z/n\mathbb Z$, $[x]_{mn}\mapsto([x]_m,[x]_n)$ è un omomorfismo di anelli (ed è un isomorfismo se $\gcd(m,n)=1$).
- $a\mapsto a+1$ da $\mathbb Z$ in sé **non** è un omomorfismo di gruppi: $g(a+b)=a+b+1\neq a+b+2$.

## Come si dimostra

Per costruire un omomorfismo con dominio un quoziente occorre controllare la [[Buona definizione|buona definizione]]; un esempio completo è nella lezione [[2026-10-22 - Omomorfismi tra anelli e teorema cinese#La mappa naturale|del 22 ottobre]].

## Vedi anche

- [[Isomorfismo]]
- [[Nucleo]]
- [[Prodotto diretto]]
- [[Buona definizione]]
