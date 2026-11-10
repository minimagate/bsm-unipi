---
title: Estremo superiore
type: voce
categoria: definizione
corsi:
- Analisi 1
introdotta_in: 2026-09-28 - Assiomi dei reali e proprietà di completezza
alias:
- supremo
- estremo inferiore
- infimo
- sup
- inf
sintesi: L'estremo superiore di un insieme è il più piccolo dei suoi maggioranti e l'estremo inferiore è il più grande dei suoi minoranti.
---
L'**estremo superiore** (o supremo) di $A\ne\varnothing$ è il più piccolo dei maggioranti; l'**estremo inferiore** (o infimo) è il più grande dei minoranti.

## Definizione

Se $A$ non è limitato superiormente si pone $\sup A=+\infty$; altrimenti

$$
\sup A=\min\{\text{maggioranti di }A\}.
$$

Analogamente $\inf A=-\infty$ se $A$ non è limitato inferiormente, e altrimenti $\inf A=\max\{\text{minoranti di }A\}$. L'esistenza di questi minimo e massimo è garantita dall'[[Assioma di completezza]].

**Caratterizzazione.** $\sup A=L\in\mathbb{R}$ se e solo se (i) $L$ è un [[Maggiorante|maggiorante]] di $A$ e (ii) per ogni $\varepsilon>0$ esiste $a\in A$ con $a>L-\varepsilon$. Inoltre $\sup A=+\infty$ se e solo se $\forall M\ \exists a\in A$ con $a>M$.

## Intuizione

Il supremo è il "punto più a destra possibile", anche quando non appartiene all'insieme: si può avvicinare quanto si vuole con elementi di $A$. Se esiste il [[Massimo e minimo|massimo]], coincide con il supremo.

## Esempi

- $\sup(0,1)=1$ e $\inf(0,1)=0$, anche se $(0,1)$ non ha massimo né minimo.
- $\sup\mathbb{N}=+\infty$.

## Come si dimostra

L'esistenza segue dalla completezza applicata ad $A$ e all'insieme dei suoi maggioranti: [[2026-09-28 - Assiomi dei reali e proprietà di completezza#14. Dimostrazione dell’esistenza del supremo|dimostrazione dell'esistenza del supremo]].

## Vedi anche

- [[Maggiorante]]
- [[Massimo e minimo]]
- [[Assioma di completezza]]
- [[Successione monotona]]
