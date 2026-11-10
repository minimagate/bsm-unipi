---
title: Principio di risoluzione
type: voce
categoria: teorema
corsi:
- Fondamenti di Programmazione
introdotta_in: 2026-09-23 - Forme normali, tecniche di dimostrazione e logica del primo ordine
alias:
- risoluzione
sintesi: Da due clausole che contengono una variabile in forma positiva e negativa si ricava la clausola ottenuta eliminando quella variabile.
---

Il **principio di risoluzione** permette di eliminare una variabile che compare positivamente in una clausola e negativamente in un'altra.

## Enunciato

$$
(P\lor Q)\land(\neg P\lor R)\Rightarrow(Q\lor R).
$$

In forma più generale:

$$
(P\lor Q_1\lor\cdots\lor Q_n)
\land
(\neg P\lor R_1\lor\cdots\lor R_k)
\Rightarrow
Q_1\lor\cdots\lor Q_n\lor R_1\lor\cdots\lor R_k.
$$

Un caso particolare utile è $(P\lor Q_1\lor\cdots\lor Q_n)\land\neg P\Rightarrow Q_1\lor\cdots\lor Q_n$.

## Intuizione

Se vale $P\lor Q$ e vale anche $\neg P\lor R$, o $P$ è vera (e allora $R$ deve esserlo) oppure $P$ è falsa (e allora lo è $Q$). In ogni caso almeno una tra $Q$ e $R$ è vera. È un'estensione del modus ponens alle clausole, ed è il meccanismo di calcolo alla base della **programmazione logica**. Lavora su formule in [[Forma normale|forma normale congiuntiva]].

## Esempi

Per provare che $((P\lor Q)\land(\neg P\lor R)\land(\neg Q\lor R))\Rightarrow R$ è una tautologia si applica la risoluzione due volte:

$$
(P\lor Q)\land(\neg P\lor R)\land(\neg Q\lor R)
\Rightarrow(Q\lor R)\land(\neg Q\lor R)
\Rightarrow R\land R\equiv R.
$$

## Come si dimostra

Basta riscrivere le disgiunzioni come implicazioni: $(P\lor Q)\land(\neg P\lor R)\equiv(\neg Q\Rightarrow P)\land(P\Rightarrow R)$, da cui, per transitività, $\neg Q\Rightarrow R\equiv Q\lor R$. La derivazione completa è nella lezione: [[2026-09-23 - Forme normali, tecniche di dimostrazione e logica del primo ordine#3. Principio di risoluzione|principio di risoluzione]].

## Vedi anche

- [[Forma normale]]
- [[Implicazione]]
- [[Tautologia]]
- [[Regola di inferenza]]
