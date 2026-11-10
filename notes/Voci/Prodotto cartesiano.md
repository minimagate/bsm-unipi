---
title: Prodotto cartesiano
type: voce
categoria: definizione
corsi:
- Analisi 1
- Aritmetica
- Geometria 1
introdotta_in: 2026-09-23 - Proposizioni, quantificatori e prime operazioni tra insiemi
alias:
- prodotto cartesiano di insiemi
sintesi: Il prodotto cartesiano di due insiemi è l'insieme di tutte le coppie ordinate con il primo elemento nel primo insieme e il secondo nel secondo.
---
Il **prodotto cartesiano** di due insiemi $A$ e $B$ è l'insieme delle coppie ordinate che hanno come prima componente un elemento di $A$ e come seconda un elemento di $B$.

## Definizione

$$
A\times B=\{(a,b) : a\in A\land b\in B\}.
$$

Le coppie sono *ordinate*: in generale $(a,b)\ne(b,a)$. Se $A=B$ si scrive $A\times A$.

## Intuizione

È la generalizzazione del piano cartesiano: $\mathbb{R}\times\mathbb{R}$ è l'insieme dei punti $(x,y)$. Il grafico di una funzione $f\colon A\to B$ è un sottoinsieme di $A\times B$.

In particolare il prodotto cartesiano è la base per definire in modo rigoroso una funzione: una funzione $f\colon A\to B$ è un sottoinsieme $G\subseteq A\times B$ tale che per ogni $a\in A$ esiste un solo $b\in B$ con $(a,b)\in G$.

## Esempi

Se $A=\{3,*,\square\}$ e $B=\{0,2\}$ allora

$$
A\times B=\{(3,0),(3,2),(*,0),(*,2),(\square,0),(\square,2)\},
$$

un insieme con $3\cdot2=6$ elementi.

## Vedi anche

- [[Insieme]]
- [[Operazioni tra insiemi]]
- [[Funzione]]
- [[Insieme delle parti]]
