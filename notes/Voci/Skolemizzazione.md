---
title: Skolemizzazione
type: voce
categoria: metodo
corsi:
- Fondamenti di Programmazione
introdotta_in: 2026-10-13 - Quantificazione ristretta, uguaglianza e specifiche formali
alias:
- Skolem
- generalizzazione
sintesi: Regola per dimostrare usando un'ipotesi esistenziale, dando un nome nuovo al testimone; la generalizzazione fa lo stesso per le tesi universali.
---

La **skolemizzazione** è una regola di inferenza per lavorare con quantificatori esistenziali. Con la **generalizzazione**, sua gemella per l'universale, forma la coppia di regole per i quantificatori.

## Enunciato

**Skolemizzazione.** Se $(\exists x.\,P)\in\Gamma$ e $\Gamma,P[d/x]\vdash Q$ con $d$ una costante **nuova**, allora $\Gamma\vdash Q$:

$$
\frac{(\exists x.\,P)\in\Gamma\quad\Gamma,P[d/x]\vdash Q\quad d\text{ nuova costante}}{\Gamma\vdash Q}.
$$

**Generalizzazione.** Per dimostrare $(\forall x.\,P)$ basta dimostrare $P[d/x]$ con $d$ nuova costante:

$$
\frac{\Gamma\vdash P[d/x]\quad d\text{ nuova costante}}{\Gamma\vdash(\forall x.\,P)}.
$$

## Intuizione

Sapere $\exists x.\,P$ significa che un elemento con la proprietà $P$ c'è, ma non si sa quale: lo si battezza $d$ e si ragiona su $d$ senza fare altre assunzioni (è un **testimone**). Nella generalizzazione, $d$ è un elemento generico del dominio: proprio perché non si sa nulla di lui, ciò che si prova per $d$ vale per tutti. La costante deve essere nuova, cioè non comparire in $\Gamma$ né in $P$.

## Esempi

Per dimostrare $(\forall x.\,P\Rightarrow Q)\land(\exists x.\,P)\Rightarrow(\exists x.\,Q)$ si aggiunge $P[d/x]$ come ipotesi, si usa l'eliminazione dell'universale per avere $P[d/x]\Rightarrow Q[d/x]$, il modus ponens per ottenere $Q[d/x]$ e infine l'introduzione dell'esistenziale per concludere $\exists x.\,Q$.

Per la generalizzazione: da $\forall x.\,P\Rightarrow Q$ e $\forall x.\,P$, con $d$ nuova si ottiene $Q[d/x]$ e per generalizzazione $\forall x.\,Q$.

## Vedi anche

- [[Regola di inferenza]]
- [[Quantificatore]]
- [[Teorema di deduzione]]
- [[Variabile libera e legata]]
