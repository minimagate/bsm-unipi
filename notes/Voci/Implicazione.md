---
title: Implicazione
type: voce
categoria: definizione
corsi:
- Analisi 1
- Fondamenti di Programmazione
introdotta_in: 2026-09-21 - Semantica del calcolo proposizionale e dimostrazioni per equivalenza
alias:
- implicazione logica
- condizione necessaria
- condizione sufficiente
- doppia implicazione
sintesi: Il connettivo "se P allora Q", falso solo quando P è vera e Q è falsa.
---

L'**implicazione** $P\Rightarrow Q$ si legge "se $P$ allora $Q$": è il [[Connettivo logico|connettivo]] che formalizza il passaggio da una premessa a una conseguenza.

## Definizione

$P\Rightarrow Q$ è falsa se e solo se $P$ è vera e $Q$ è falsa:

| $P$ | $Q$ | $P\Rightarrow Q$ |
|---|---|---|
| $\mathsf t$ | $\mathsf t$ | $\mathsf t$ |
| $\mathsf t$ | $\mathsf f$ | $\mathsf f$ |
| $\mathsf f$ | $\mathsf t$ | $\mathsf t$ |
| $\mathsf f$ | $\mathsf f$ | $\mathsf t$ |

Equivalentemente, $(P\Rightarrow Q)\equiv\neg(P\land\neg Q)\equiv\neg P\lor Q$. Vale anche $P\equiv Q$ se e solo se $(P\Rightarrow Q)\land(Q\Rightarrow P)$ (doppia implicazione).

## Intuizione

L'implicazione afferma che ogni situazione in cui $P$ è vera è anche una situazione in cui $Q$ è vera. L'unico caso che la smentisce è "$P$ vera e $Q$ falsa". Se $P$ è falsa non c'è niente da smentire e l'implicazione è vera ("vacuamente"). In «$P\Rightarrow Q$», $P$ è una condizione **sufficiente** per $Q$ e $Q$ è una condizione **necessaria** per $P$; «$P$ solo se $Q$» si traduce proprio $P\Rightarrow Q$.

## Esempi

- «Condizione necessaria affinché Antonio vada al cinema è che ci vada Bruno» si scrive $a\Rightarrow b$.
- «Se $x$ è pari, allora $x+1$ è dispari» è vera anche per $x=3$, perché la premessa è falsa.

## Vedi anche

- [[Connettivo logico]]
- [[Contrapposizione]]
- [[Equivalenza logica]]
- [[Conseguenza logica]]
