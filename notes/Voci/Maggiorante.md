---
title: Maggiorante
type: voce
categoria: definizione
corsi:
- Analisi 1
introdotta_in: 2026-09-28 - Assiomi dei reali e proprietà di completezza
alias:
- minorante
- maggioranti
- minoranti
- insieme limitato
sintesi: Un maggiorante di un insieme è un numero maggiore o uguale a tutti i suoi elementi, un minorante è minore o uguale a tutti; un insieme con entrambi è limitato.
---
Un **maggiorante** di un insieme $A\subseteq\mathbb{R}$ è una "barriera dall'alto": un numero maggiore o uguale a tutti gli elementi di $A$. Un **minorante** è una barriera dal basso.

## Definizione

- $M$ è un maggiorante di $A$ se $\forall a\in A,\ a\le M$;
- $m$ è un minorante di $A$ se $\forall a\in A,\ m\le a$.

$A$ è **limitato superiormente** se ha almeno un maggiorante, **limitato inferiormente** se ha almeno un minorante, **limitato** se ha entrambi. Equivalentemente, $A$ è limitato se $\exists L$ tale che $|a|\le L$ per ogni $a\in A$.

## Intuizione

I maggioranti non sono unici (se $M$ lo è, anche ogni $M'\ge M$) e non devono appartenere ad $A$. Quando uno appartiene ad $A$, è il [[Massimo e minimo|massimo]]; il più piccolo dei maggioranti è l'[[Estremo superiore|estremo superiore]].

## Esempi

- Per $A=(0,1)$ i maggioranti sono tutti i numeri $M\ge1$ e i minoranti tutti i numeri $m\le0$.
- $\mathbb{R}$ non ha maggioranti; ogni numero reale è un maggiorante di $\varnothing$.

## Vedi anche

- [[Massimo e minimo]]
- [[Estremo superiore]]
- [[Assioma di completezza]]
- [[Valore assoluto]]
