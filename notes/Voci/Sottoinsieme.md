---
title: Sottoinsieme
type: voce
categoria: definizione
corsi:
- Analisi 1
- Aritmetica
- Geometria 1
introdotta_in: 2026-09-23 - Proposizioni, quantificatori e prime operazioni tra insiemi
alias:
- inclusione
- inclusione tra insiemi
- sottoinsiemi
sintesi: Un insieme A è sottoinsieme di B se ogni elemento di A è anche elemento di B.
---
Un **sottoinsieme** di $B$ è un insieme $A$ i cui elementi stanno tutti anche in $B$. La relazione si chiama *inclusione*.

## Definizione

$$
A\subseteq B\quad\Longleftrightarrow\quad\forall x\,(x\in A\Rightarrow x\in B).
$$

Se inoltre $A\ne B$ si scrive $A\subsetneq B$ (inclusione propria). Per evitare ambiguità si evita il simbolo $\subset$, che alcuni testi usano per l'una e altri per l'altra.

## Intuizione

L'inclusione è una relazione tra *due insiemi*, mentre $x\in A$ è una relazione tra *un elemento e un insieme*. Non vanno confuse: $3\in\{3,*\}$ ma $\{3\}\subseteq\{3,*\}$.

L'insieme vuoto è contenuto in ogni insieme: l'implicazione $x\in\varnothing\Rightarrow x\in A$ ha premessa sempre falsa, quindi è sempre vera.

Per dimostrare che $A\subseteq B$ si prende un elemento qualsiasi $x\in A$ e si mostra che sta in $B$; per dimostrare che $A\not\subseteq B$ basta esibire un elemento di $A$ che non sta in $B$.

## Esempi

- $\{2,3\}\subseteq\{1,2,3\}$, anzi $\{2,3\}\subsetneq\{1,2,3\}$.
- $\mathbb{N}\subseteq\mathbb{Z}\subseteq\mathbb{Q}\subseteq\mathbb{R}$.
- $\varnothing\subseteq A$ per ogni insieme $A$.

## Vedi anche

- [[Insieme]]
- [[Insieme delle parti]]
- [[Implicazione]]
- [[Operazioni tra insiemi]]
