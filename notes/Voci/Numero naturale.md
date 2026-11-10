---
title: Numero naturale
type: voce
categoria: oggetto
corsi:
- Aritmetica
introdotta_in: 2026-09-23 - Numeri naturali, induzione e fattorizzazione
alias:
- numeri naturali
- assiomi di Peano
sintesi: I numeri naturali sono i numeri con cui si conta, a partire da zero, ottenuti dallo zero passando di volta in volta al successore.
---

I **numeri naturali** sono i numeri che usiamo per contare: $0,1,2,3,\ldots$ L'insieme di tutti i naturali si indica con $\mathbb{N}$ e, in questo corso, contiene lo zero.

## Definizione

Nella presentazione assiomatica (assiomi di Peano) i naturali sono dati da:

1. un elemento iniziale, $0$;
2. un'operazione di successore, che a ogni $n$ associa $n+1$;
3. il principio che permette di ottenere ogni naturale partendo da $0$ e applicando un numero finito di volte il successore (da qui nasce l'[[Principio di induzione|induzione]]).

Inoltre $0$ non è successore di nessun naturale e naturali distinti hanno successori distinti. I naturali sono chiusi rispetto alla somma e al prodotto, ma non alla sottrazione: $x+3=0$ non ha soluzione in $\mathbb{N}$.

## Intuizione

Pensa a una fila infinita di tessere del domino numerate: si parte da $0$ e ogni tessera ha una successiva. È proprio questa struttura "a fila" che rende possibili le dimostrazioni per induzione e che garantisce il [[Principio del minimo]].

## Esempi

- Il successore di $4$ è $5$; $0$ non è successore di nessuno.
- L'equazione $x+3=0$ non ha soluzioni naturali: per risolverla serve passare agli interi $\mathbb{Z}$.
- Per contare gli oggetti di un insieme finito si usa una biezione con $\{1,\dots,n\}$ (vedi [[Cardinalità]]).

## Come si dimostra

La costruzione assiomatica è descritta [[2026-09-23 - Numeri naturali, induzione e fattorizzazione#3. Definizione assiomatica dei numeri naturali|nella lezione del 23 settembre]].

## Vedi anche

- [[Principio di induzione]]
- [[Principio del minimo]]
- [[Cardinalità]]
- [[Numero primo]]
