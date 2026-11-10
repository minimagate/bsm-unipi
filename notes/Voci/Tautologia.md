---
title: Tautologia
type: voce
categoria: definizione
corsi:
- Fondamenti di Programmazione
introdotta_in: 2026-09-21 - Semantica del calcolo proposizionale e dimostrazioni per equivalenza
alias:
- tautologie
- contraddizione
- soddisfacibilità
sintesi: Formula vera in ogni interpretazione; la sua negazione è una contraddizione, vera in nessuna.
---

Una **tautologia** è una formula del [[Calcolo proposizionale|calcolo proposizionale]] che è vera in ogni [[Interpretazione|interpretazione]]. Si scrive $\models\varphi$.

## Definizione

Sia $\varphi$ una formula.

- $\varphi$ è **soddisfacibile** se esiste almeno un'interpretazione $I$ con $I\models\varphi$;
- $\varphi$ è una **tautologia** se è vera in ogni interpretazione;
- $\varphi$ è una **contraddizione** (o **insoddisfacibile**) se è falsa in ogni interpretazione.

In particolare $\varphi$ è una tautologia se e solo se $\neg\varphi$ è una contraddizione.

## Intuizione

Le tautologie sono le "leggi" della logica: formule vere per pura forma, qualunque cosa dicano i simboli. Per mostrare che una formula **non** è una tautologia basta un solo controesempio, cioè un'interpretazione che la rende falsa; per mostrare che lo è servono tutte le righe di una [[Tavola di verità|tavola di verità]] oppure una dimostrazione.

## Esempi

- $p\lor\neg p$ (terzo escluso) è una tautologia; $p\land\neg p$ è una contraddizione.
- $((a\Rightarrow b)\land a)\Rightarrow b$ (modus ponens) è una tautologia.
- $((a\Rightarrow b)\land\neg a)\Rightarrow b$ non lo è: con $a\mapsto\mathsf f$, $b\mapsto\mathsf f$ la premessa è vera e la conclusione falsa.
- $p\land q$ è soddisfacibile ma non è una tautologia.

## Vedi anche

- [[Equivalenza logica]]
- [[Conseguenza logica]]
- [[Tavola di verità]]
- [[Interpretazione]]
