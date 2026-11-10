---
title: Insieme
type: voce
categoria: oggetto
corsi:
- Analisi 1
- Aritmetica
- Geometria 1
introdotta_in: 2026-09-23 - Proposizioni, quantificatori e prime operazioni tra insiemi
alias:
- insiemi
sintesi: Un insieme è una collezione di oggetti, detti elementi, che si descrive elencandoli oppure indicando la proprietà che li caratterizza.
---
Un **insieme** è una collezione di oggetti, detti *elementi*. In questo corso non si dà una definizione formale: si usa l'idea intuitiva.

## Definizione

Un insieme si può presentare:

- **per elencazione**: $A=\{2,3\}$;
- **per proprietà caratteristica**: $B=\{s : s \text{ è uno studente di Analisi 1 a Pisa}\}$, dove "$:$" si legge "tale che".

Si scrive $x\in A$ se $x$ è un elemento di $A$, e $x\notin A$ altrimenti. L'insieme vuoto $\varnothing$ non ha elementi.

## Intuizione

Un insieme non è una lista: l'ordine non conta e le ripetizioni sono ignorate. Quindi $\{2,3\}=\{3,2\}$ e $\{2,2,3\}=\{2,3\}$.

In pratica, quando si scrive un insieme per proprietà conviene sempre dire da dove si pescano gli elementi (per esempio $m\in\mathbb{N}$ tale che esiste $a\in\mathbb{Z}$ con $m=a^2$): così il predicato che definisce l'insieme ha una sola variabile libera e ha un significato preciso.

## Esempi

- $A=\{n^2 : n\in\mathbb{Z}\}=\{0,1,4,9,16,\dots\}$: il valore $1$ compare sia da $1^2$ sia da $(-1)^2$ ma è un solo elemento.
- Fare attenzione: $\varnothing$ ha zero elementi, mentre $\{\varnothing\}$ ne ha uno (l'insieme vuoto).

## Vedi anche

- [[Sottoinsieme]]
- [[Operazioni tra insiemi]]
- [[Prodotto cartesiano]]
- [[Insieme delle parti]]
