---
title: Modello di von Neumann
type: voce
categoria: oggetto
corsi:
- Fondamenti di Programmazione
introdotta_in: 2026-09-19 - Pensiero computazionale, algoritmi e modelli di calcolo
alias:
- von Neumann
- architettura di von Neumann
sintesi: Modello concreto di architettura dei calcolatori basato sul programma memorizzato, equivalente alla macchina di Turing quanto a capacità di calcolo.
---

Il **modello di von Neumann**, introdotto intorno al 1945, è il modello concreto di architettura su cui si basano i calcolatori attuali.

## Definizione

La sua idea centrale è il **programma memorizzato**: il programma sta in memoria insieme ai dati, e la stessa macchina può quindi eseguire calcoli diversi cambiando solo il programma. Quanto a capacità di calcolo è equivalente alla [[Macchina di Turing|macchina di Turing]].

## Intuizione

È la versione "da officina" della macchina di Turing universale. Per i nostri scopi conta soprattutto un fatto: lo [[Stato|stato]] di un calcolatore si può pensare come il contenuto della memoria, e ogni passo di esecuzione lo modifica. Nel paradigma imperativo, e poi in C, l'**assegnamento** è proprio l'azione che modifica una parte della memoria.

## Esempi

Se la memoria contiene $A\mapsto 5$, $B\mapsto 3$, $C\mapsto 0$, eseguire "somma $A$ a $C$" la porta a $C\mapsto 5$: è un passaggio da uno stato al successivo.

## Vedi anche

- [[Macchina di Turing]]
- [[Tesi di Church-Turing]]
- [[Stato]]
- [[Algoritmo]]
