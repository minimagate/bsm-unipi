---
title: Quantificatore
type: voce
categoria: notazione
corsi:
- Analisi 1
- Fondamenti di Programmazione
introdotta_in: 2026-09-23 - Proposizioni, quantificatori e prime operazioni tra insiemi
alias:
- quantificatori
- quantificatore universale
- quantificatore esistenziale
sintesi: I quantificatori per ogni ed esiste permettono di trasformare un predicato in una proposizione dicendo per quali valori delle variabili vale.
---
I **quantificatori** sono i simboli $\forall$ ("per ogni") ed $\exists$ ("esiste almeno un") che si premettono a un predicato per dire *per quanti* valori della variabile esso vale.

## Definizione

Dato un predicato $P(x)$:

- $\forall x\ P(x)$ è vera se $P(x)$ è vera per ogni $x$ (**quantificatore universale**);
- $\exists x\ P(x)$ è vera se esiste almeno un $x$ per cui $P(x)$ è vera (**quantificatore esistenziale**).

Un predicato diventa una [[Proposizione|proposizione]] quando tutte le sue variabili sono quantificate o sostituite.

Le negazioni seguono le [[Leggi di De Morgan|leggi di De Morgan]] estese ai quantificatori:

$$
\neg\forall x\,P(x)\equiv\exists x\,\neg P(x),\qquad
\neg\exists x\,P(x)\equiv\forall x\,\neg P(x).
$$

## Intuizione

"$\forall$" è una promessa su *tutti* i casi, e per smontarla basta un controesempio. "$\exists$" è una promessa su *almeno un* caso, e per smontarla bisogna escluderli tutti.

L'**ordine** dei quantificatori conta: $\forall S\,\exists B\,P(S,B)$ ("ogni studente ha una birra preferita") non dice la stessa cosa di $\exists B\,\forall S\,P(S,B)$ ("c'è una birra che piace a tutti").

## Esempi

- $\forall x\in\mathbb{R},\ x\ge 3$ è falsa ($x=0$ è un controesempio).
- La negazione di "a ogni studente piace almeno una birra", cioè $\forall S\,\exists B\,P(S,B)$, è $\exists S\,\forall B\,\neg P(S,B)$: esiste uno studente a cui non piace nessuna birra.

## Vedi anche

- [[Proposizione]]
- [[Leggi di De Morgan]]
- [[Implicazione]]
- [[Quantificazione ristretta]]
