---
title: Interpretazione
type: voce
categoria: definizione
corsi:
- Fondamenti di Programmazione
introdotta_in: 2026-09-21 - Semantica del calcolo proposizionale e dimostrazioni per equivalenza
alias:
- interpretazioni
- modello
- modelli
- funzione di valutazione
sintesi: Assegnazione di un significato ai simboli di una formula, che permette di calcolarne il valore di verità.
---

Un'**interpretazione** attribuisce un significato ai simboli di una formula, e quindi permette di dire se la formula è vera o falsa. Senza interpretazione una formula è solo una stringa di simboli.

## Definizione

Nel [[Calcolo proposizionale|calcolo proposizionale]] un'interpretazione è una funzione $I:\mathcal P\to\mathrm{Bool}$ che assegna un valore booleano a ogni simbolo proposizionale, per esempio $I=\{p\mapsto\mathsf t,\ q\mapsto\mathsf f,\ r\mapsto\mathsf f\}$. Fissata $I$, il valore di una formula è dato dalla **funzione di valutazione** $\llbracket\cdot\rrbracket_I:\mathrm{Prop}\to\mathrm{Bool}$, definita ricorsivamente, per esempio $\llbracket P\land Q\rrbracket_I=\llbracket P\rrbracket_I\land\llbracket Q\rrbracket_I$.

Se $\llbracket\varphi\rrbracket_I=\mathsf t$ si dice che $I$ è un **modello** di $\varphi$ e si scrive $I\models\varphi$.

Nella [[Logica del primo ordine|logica del primo ordine]] un'interpretazione è una coppia $\mathcal I=(D,\alpha)$: un dominio $D$ e una funzione $\alpha$ che dà un significato a costanti, simboli di funzione e predicati.

## Intuizione

La stessa formula può essere vera in un'interpretazione e falsa in un'altra. Per esempio $P(A)$ è vera se $P$ significa "essere un essere umano" e $A$ è il filosofo Socrate, ma falsa se $A$ è un cane che si chiama Socrate. La dimostrazione, invece, lavora solo sui simboli, senza guardare l'interpretazione.

## Esempi

Per $\varphi=(p\land q)\lor\neg r$ e $I=\{p\mapsto\mathsf t,\ q\mapsto\mathsf f,\ r\mapsto\mathsf f\}$:

$$
\llbracket\varphi\rrbracket_I=(\mathsf t\land\mathsf f)\lor\neg\mathsf f=\mathsf f\lor\mathsf t=\mathsf t.
$$

## Vedi anche

- [[Conseguenza logica]]
- [[Tautologia]]
- [[Tavola di verità]]
- [[Logica del primo ordine]]
