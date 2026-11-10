---
title: Precondizione e postcondizione
type: voce
categoria: definizione
corsi:
- Fondamenti di Programmazione
introdotta_in: 2026-10-19 - Espressioni, comandi e triple di Hoare
alias:
- precondizione
- postcondizione
- precondizioni
- postcondizioni
sintesi: La precondizione descrive gli stati da cui si parte e la postcondizione quelli che si vogliono ottenere alla fine dell'esecuzione.
---
La **precondizione** e la **postcondizione** sono le due asserzioni che incorniciano un comando in una [[Tripla di Hoare|tripla di Hoare]]: la prima dice che cosa deve valere prima dell'esecuzione, la seconda che cosa si garantisce dopo.

## Definizione

In $\{Q\}\ C\ \{R\}$, $Q$ è la precondizione e $R$ la postcondizione. Sono formule della logica del primo ordine; $\{P\}$ indica anche l'insieme degli stati che le soddisfano, $\{P\}=\{\sigma\mid\sigma\models P\}$. Una precondizione più forte (cioè con meno stati) restringe i casi da gestire; una postcondizione più forte promette di più.

## Intuizione

La precondizione è il patto che il chiamante deve rispettare, la postcondizione è ciò che il programma garantisce in cambio. Rafforzare la precondizione o indebolire la postcondizione rende più facile dimostrare la tripla, a spese di una specifica meno utile. Si può sempre fare, come dicono le regole $(\mathrm{pre})$ e $(\mathrm{post})$: se $P\Rightarrow P'$ e $\{P'\}\,C\,\{R\}$ vale, allora vale anche $\{P\}\,C\,\{R\}$.

## Esempi

- Per la divisione intera con sottrazioni: $Q:\ x\geq0\land y>0$ e $R:\ x=y\cdot q+r\land0\leq r<y$.
- Se la guardia di un `if` contiene `x div y`, la precondizione $x\geq0\land y\geq0$ non basta, perché con $y=0$ la guardia non è definita: va rafforzata in $x\geq0\land y>0$.

## Vedi anche

- [[Tripla di Hoare]]
- [[Specifica di un problema]]
- [[Regola dell'assegnamento]]
- [[Correttezza totale]]
