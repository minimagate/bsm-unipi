---
title: Punto di accumulazione
type: voce
categoria: definizione
corsi:
- Analisi 1
introdotta_in: 2026-10-12 - Limiti di funzioni, continuità e limiti notevoli
alias:
- punti di accumulazione
sintesi: Un punto vicino al quale cadono sempre altri punti dell'insieme, così che ha senso calcolare il limite di una funzione.
---

Un **punto di accumulazione** di un insieme $D\subseteq\mathbb{R}$ è un punto $x_0$ vicino al quale, comunque piccolo sia l'intervallo, si trovano punti di $D$ diversi da $x_0$. È la condizione che rende sensato parlare di [[Limite di una funzione|limite]] in $x_0$.

## Definizione

$x_0\in\mathbb{R}$ è punto di accumulazione di $D$ se

$$
\forall\delta>0\qquad \bigl(D\cap[x_0-\delta,x_0+\delta]\bigr)\setminus\{x_0\}\neq\emptyset.
$$

In parole: in ogni intervallo centrato in $x_0$ c'è almeno un punto di $D$ diverso da $x_0$ stesso.

## Intuizione

Per calcolare un limite in $x_0$ servono punti di $D$ che si avvicinano a $x_0$ quanto si vuole: se non ce ne sono, non c'è nessun comportamento da "prevedere". Per questo la definizione toglie $x_0$ dall'intervallo: conta solo chi gli sta intorno.

Occhio: $x_0$ non deve per forza appartenere a $D$, e un punto isolato di $D$ appartiene a $D$ ma non è di accumulazione.

## Esempi

- Per $D=(0,1)$ ogni punto di $[0,1]$ è di accumulazione, anche $0$ e $1$ che non stanno in $D$.
- Per $D=\mathbb{N}$ nessun punto reale è di accumulazione: i numeri naturali sono tutti isolati.
- Per $D=\{1/n:n\geq1\}$ l'unico punto di accumulazione è $0$.

## Vedi anche

- [[Limite di una funzione]]
- [[Funzione continua]]
- [[Insieme]]
