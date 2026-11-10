---
title: Operazioni tra insiemi
type: voce
categoria: definizione
corsi:
- Analisi 1
- Aritmetica
- Geometria 1
introdotta_in: 2026-09-23 - Proposizioni, quantificatori e prime operazioni tra insiemi
alias:
- unione
- intersezione
- differenza tra insiemi
- unione di insiemi
- intersezione di insiemi
sintesi: Unione, intersezione e differenza permettono di costruire nuovi insiemi a partire da due insiemi dati.
---
Le **operazioni tra insiemi** più semplici sono l'unione, l'intersezione e la differenza. Si definiscono con i connettivi logici applicati all'appartenenza.

## Definizione

Dati due [[Insieme|insiemi]] $A$ e $B$:

$$
A\cap B=\{x : x\in A\land x\in B\}\quad\text{(intersezione)},
$$

$$
A\cup B=\{x : x\in A\lor x\in B\}\quad\text{(unione)},
$$

$$
A\setminus B=\{x : x\in A\land x\notin B\}\quad\text{(differenza)}.
$$

## Intuizione

- L'intersezione contiene gli elementi *comuni*.
- L'unione contiene gli elementi che stanno in *almeno uno* dei due (l'"oppure" è inclusivo).
- La differenza toglie da $A$ tutto ciò che sta in $B$. L'ordine conta: in generale $A\setminus B\ne B\setminus A$.

Le tre operazioni corrispondono ai connettivi logici: l'intersezione a "e", l'unione a "oppure" e la differenza a "e non". Per questo le leggi di De Morgan si traducono in regole sul complementare di unioni e intersezioni.

## Esempi

Con $A=\{1,2,3\}$ e $B=\{2,3,4\}$:

- $A\cap B=\{2,3\}$;
- $A\cup B=\{1,2,3,4\}$;
- $A\setminus B=\{1\}$ e $B\setminus A=\{4\}$.

## Vedi anche

- [[Insieme]]
- [[Sottoinsieme]]
- [[Prodotto cartesiano]]
- [[Connettivo logico]]
