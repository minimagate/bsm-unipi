---
title: Calcolo proposizionale
type: voce
categoria: oggetto
corsi:
- Analisi 1
- Fondamenti di Programmazione
introdotta_in: 2026-09-21 - Semantica del calcolo proposizionale e dimostrazioni per equivalenza
alias:
- CP
- logica proposizionale
sintesi: Il più semplice linguaggio logico formale, in cui si costruiscono formule complesse a partire da simboli proposizionali e connettivi.
---

Il **calcolo proposizionale** (CP) è il più semplice linguaggio logico formale: permette di rappresentare proposizioni vere o false e di combinarle con i connettivi. È il nucleo su cui si costruiscono linguaggi più potenti, come la [[Logica del primo ordine|logica del primo ordine]].

## Definizione

Dato un alfabeto $\mathcal P=\{p,q,r,\ldots\}$ di simboli proposizionali, le formule sono definite così:

1. $\mathrm T$ e $\mathrm F$ sono formule;
2. ogni $p\in\mathcal P$ è una formula;
3. se $P$ e $Q$ sono formule, lo sono anche $\neg P$, $(P\land Q)$, $(P\lor Q)$, $(P\Rightarrow Q)$, $(P\equiv Q)$.

La sintassi dice quali formule sono ben formate; la semantica, data da un'[[Interpretazione|interpretazione]], ne calcola il valore di verità.

## Intuizione

Le proposizioni atomiche sono "mattoncini indivisibili" («piove», «Antonio va al cinema»), i [[Connettivo logico|connettivi]] sono i modi di incollarli. Il prezzo della semplicità è che non si può parlare di individui, proprietà o di "tutti" e "qualcuno": per questo poi serve la logica del primo ordine.

## Esempi

La frase «se piove e non c'è vento, allora ci si copre» si formalizza con $(p\land\neg v)\Rightarrow c$. Per $\varphi=(p\land q)\lor\neg r$, con $p\mapsto\mathsf t$, $q\mapsto\mathsf f$, $r\mapsto\mathsf f$ si ottiene $\mathsf f\lor\mathsf t=\mathsf t$.

## Vedi anche

- [[Connettivo logico]]
- [[Interpretazione]]
- [[Tavola di verità]]
- [[Logica del primo ordine]]
