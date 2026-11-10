---
title: Specifica di un problema
type: voce
categoria: definizione
corsi:
- Fondamenti di Programmazione
introdotta_in: 2026-09-25 - Stati, algoritmi e fondamenti della logica formale
alias:
- specifica
- specifiche
- variabili di specifica
- variabile di specifica
sintesi: Descrizione di un problema come coppia di proprietà, quella dello stato iniziale con i dati e quella dello stato finale con i risultati attesi.
---

La **specifica** di un problema ne dice che cosa si vuole ottenere, senza dire come ottenerlo.

## Definizione

Una specifica è una coppia di descrizioni:

$$
\text{(proprietà dello) stato iniziale}\ \longrightarrow\ \text{(proprietà dello) stato finale}.
$$

Lo [[Stato|stato]] iniziale descrive i dati in ingresso, quello finale i risultati attesi. Per parlare dei valori iniziali anche dopo che le variabili sono state modificate si usano le **variabili di specifica** (di solito maiuscole), che non possono essere cambiate dal programma:

$$
x=X\land y=Y\land X\ge0\land Y\ge0\ \longrightarrow\ z=X\max Y.
$$

## Intuizione

Senza variabili di specifica una specifica può essere troppo debole: un "algoritmo" che da $\{x\mapsto20,y\mapsto3\}$ arriva a $\{x\mapsto2,y\mapsto50,z\mapsto50\}$ soddisfa $z=x\max y$ pur non calcolando il massimo dei valori iniziali. Una specifica non dà il metodo risolutivo e può anche essere ambigua (ad esempio, se più persone hanno lo stesso nome in un elenco telefonico).

## Esempi

- Prodotto: $\{\mathrm{fattore1}\mapsto a,\mathrm{fattore2}\mapsto b\}\longrightarrow\{\mathrm{prodotto}\mapsto a\cdot b\}$.
- Raddoppiare un naturale: $x=A\land A>0\longrightarrow x=2\cdot A$.
- Quoziente e resto: $x=X\land y=Y\land X\ge0\land Y>0\longrightarrow X=q\cdot Y+r\land0\le r<Y$.

## Vedi anche

- [[Stato]]
- [[Precondizione e postcondizione]]
- [[Algoritmo]]
- [[Tripla di Hoare]]
