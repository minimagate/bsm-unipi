---
title: Cardinalità
type: voce
categoria: definizione
corsi:
- Analisi 1
- Aritmetica
introdotta_in: 2026-09-29 - Cardinalità e tecniche fondamentali del calcolo combinatorio
alias:
- cardinalità di un insieme
sintesi: La cardinalità di un insieme finito è il numero dei suoi elementi, cioè l'unico naturale r per cui esiste una corrispondenza biunivoca con l'insieme da uno a r.
---

La **cardinalità** di un insieme finito $X$ è il numero dei suoi elementi. Si indica con $|X|$, $\#X$ oppure $\operatorname{card}(X)$.

## Definizione

Sia $[r]=\{1,2,\ldots,r\}$. Si scrive $|X|=r$ se esiste una funzione biiettiva

$$f:[r]\longrightarrow X.$$

Due insiemi hanno la stessa cardinalità se e solo se esiste una biiezione $X\to Y$:

$$|X|=|Y|\iff\exists f:X\to Y\text{ biiettiva}.$$

Se $|X|=n$ e $|Y|=m$ valgono $|X\times Y|=nm$ e $|\mathcal{P}(X)|=2^n$.

## Intuizione

Contare significa numerare: associare a ogni elemento un numero senza saltarne e senza ripeterne. Se riesci a "appaiare" due insiemi elemento per elemento, hanno lo stesso numero di elementi, anche senza sapere quanti sono.

## Esempi

- Un insieme di cinque oggetti si numera $1,2,3,4,5$: biezione con $[5]$, quindi cardinalità $5$.
- Se $|X|>|Y|$ non esiste una funzione iniettiva $X\to Y$ ([[Principio dei cassetti]]).

## Come si dimostra

Vedi [[2026-09-29 - Cardinalità e tecniche fondamentali del calcolo combinatorio#3. Che cosa significa contare|la lezione del 29 settembre]].

## Vedi anche

- [[Funzione biettiva]]
- [[Principio dei cassetti]]
- [[Insieme delle parti]]
- [[Prodotto cartesiano]]
