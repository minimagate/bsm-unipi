---
title: Tavola di verità
type: voce
categoria: metodo
corsi:
- Analisi 1
- Fondamenti di Programmazione
introdotta_in: 2026-09-21 - Semantica del calcolo proposizionale e dimostrazioni per equivalenza
alias:
- tavole di verità
sintesi: Tabella che elenca il valore di verità di una formula per ogni possibile interpretazione dei suoi simboli proposizionali.
---

Una **tavola di verità** elenca il valore di una formula per ciascuna interpretazione dei simboli proposizionali che vi compaiono. È il metodo più diretto, e del tutto meccanico, per studiare una formula del [[Calcolo proposizionale|calcolo proposizionale]].

## Definizione

Se nella formula compaiono $n$ simboli proposizionali distinti, le [[Interpretazione|interpretazioni]] possibili sono $2^n$, e la tavola ha una riga per ciascuna. Si calcolano prima le sottoformule più semplici, poi si sale fino al [[Connettivo logico|connettivo]] principale, che dà il valore della formula.

## Intuizione

È un controllo "a forza bruta": si provano tutti i casi. Serve per verificare se una formula è una [[Tautologia|tautologia]] (vera in tutte le righe), se è soddisfacibile (vera in almeno una), o se due formule sono equivalenti (stessa colonna finale). Il limite è la crescita esponenziale: con $n$ simboli le righe sono $2^n$.

## Esempi

Per $\varphi=(p\land q)\lor\neg r$ le 8 righe danno falso solo per $(\mathsf t,\mathsf f,\mathsf t)$, $(\mathsf f,\mathsf t,\mathsf t)$ e $(\mathsf f,\mathsf f,\mathsf t)$.

Per mostrare che $P\Rightarrow Q$ e $\neg(P\land\neg Q)$ sono equivalenti basta confrontare le due colonne sulle 4 righe di $(P,Q)$: coincidono tutte.

## Vedi anche

- [[Connettivo logico]]
- [[Tautologia]]
- [[Equivalenza logica]]
- [[Interpretazione]]
