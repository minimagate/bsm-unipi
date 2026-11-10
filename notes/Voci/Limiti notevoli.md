---
title: Limiti notevoli
type: voce
categoria: teorema
corsi:
- Analisi 1
introdotta_in: 2026-10-12 - Limiti di funzioni, continuità e limiti notevoli
alias:
- limite notevole
sintesi: Una piccola famiglia di limiti fondamentali, da cui si ricavano quasi tutti gli altri limiti con seno, coseno, esponenziale e logaritmo.
---

I **limiti notevoli** sono pochi limiti standard che conviene conoscere a memoria, perché con un po' di algebra e cambi di variabile permettono di calcolare quasi tutti i limiti con funzioni elementari.

## Enunciato

Per i "padri":

$$
\lim_{x\to0}\frac{\sin x}{x}=1,\qquad \lim_{x\to+\infty}\left(1+\frac1x\right)^x=e.
$$

Per i "figli" e i "nipoti", tutti per $x\to0$:

$$
\frac{1-\cos x}{x^2}\to\frac12,\quad \frac{e^x-1}{x}\to1,\quad \frac{\log(1+x)}{x}\to1,\quad \frac{\tan x}{x},\ \frac{\arctan x}{x},\ \frac{\arcsin x}{x}\to1,
$$

$$
\frac{a^x-1}{x}\to\log a\quad(a>0),\qquad\text{e}\qquad \lim_{x\to0^+}x\log x=0.
$$

## Intuizione

Dicono che, vicino a $0$, queste funzioni si comportano come semplici polinomi: $\sin x\approx x$, $e^x-1\approx x$, $1-\cos x\approx x^2/2$. Quasi tutti sono forme $\frac00$.

La tecnica tipica è moltiplicare e dividere per la quantità giusta e fare un cambio di variabile. Riscritti con l'[[Simboli di Landau|o piccolo]] diventano gli [[Sviluppo di Taylor|sviluppi di Taylor]] di primo ordine.

## Esempi

- $\displaystyle\lim_{x\to0}\frac{e^{3x}-1}{\sin x}=\frac{e^{3x}-1}{3x}\cdot3\cdot\frac{x}{\sin x}\to3$.
- $\displaystyle\lim_{n\to\infty}n\sin\frac1n=1$, applicando il limite del seno lungo la successione $1/n$.

## Come si dimostra

Il limite del seno si dimostra con la disuguaglianza $\sin x\leq x\leq\tan x$ e i carabinieri; gli altri ne discendono con cambi di variabile (vedi [[2026-10-21 - Dimostrazioni dei limiti notevoli e applicazioni#1. Il limite fondamentale del seno|la lezione del 21 ottobre]]). Il limite con $e$ viene dal [[Numero di Nepero|numero di Nepero]].

## Vedi anche

- [[Limite di una funzione]]
- [[Numero di Nepero]]
- [[Simboli di Landau]]
- [[Teorema dei carabinieri]]
