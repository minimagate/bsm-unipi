---
title: Equivalenza logica
type: voce
categoria: definizione
corsi:
- Fondamenti di Programmazione
introdotta_in: 2026-09-21 - Semantica del calcolo proposizionale e dimostrazioni per equivalenza
alias:
- equivalenza tautologica
- equivalenze tautologiche
- formule equivalenti
sintesi: Due formule sono equivalenti quando hanno lo stesso valore di verità in ogni interpretazione.
---

Due formule $P$ e $Q$ sono **logicamente equivalenti** quando hanno lo stesso valore di verità in ogni [[Interpretazione|interpretazione]]. In altre parole, $P\equiv Q$ è una [[Tautologia|tautologia]].

## Definizione

Il connettivo $P\equiv Q$ è vero quando $P$ e $Q$ hanno lo stesso valore di verità. Si scrive $\models P\equiv Q$ per dire che le due formule sono equivalenti. L'equivalenza è riflessiva, simmetrica e transitiva, ed è anche associativa: $((P\equiv Q)\equiv R)\equiv(P\equiv(Q\equiv R))$.

## Intuizione

Due formule equivalenti sono "la stessa cosa scritta in due modi", e per questo si possono scambiare una con l'altra dentro una formula più grande (vedi il [[Principio di sostituzione|principio di sostituzione]]). Così una dimostrazione diventa una catena $P_1\equiv P_2\equiv\cdots\equiv P_n$, in cui ogni passaggio è giustificato da una legge.

## Esempi

- Le [[Leggi di De Morgan|leggi di De Morgan]]: $\neg(P\land Q)\equiv\neg P\lor\neg Q$.
- Eliminazione dell'implicazione: $P\Rightarrow Q\equiv\neg P\lor Q$.
- Legge di unità: $(P\equiv\mathrm T)\equiv P$. Con una tavola di verità basta controllare $p=\mathsf t$ e $p=\mathsf f$: in entrambi i casi la formula vale $\mathsf t$.

## Vedi anche

- [[Principio di sostituzione]]
- [[Tautologia]]
- [[Implicazione]]
- [[Forma normale]]
