---
title: Funzione inversa
type: voce
categoria: definizione
corsi:
- Analisi 1
- Aritmetica
- Geometria 1
introdotta_in: 2026-09-23 - Insiemi, applicazioni e spazi vettoriali
alias:
- inversa
- funzione invertibile
- funzioni invertibili
sintesi: L'inversa di una funzione biettiva è la funzione che riporta ogni elemento del codominio all'unico elemento da cui proviene.
---

Se $f:X\to Y$ è una [[Funzione biettiva|funzione biettiva]], la sua **inversa** è la funzione $f^{-1}:Y\to X$ che a ogni $y\in Y$ associa l'unico $x\in X$ con $f(x)=y$.

## Definizione

La funzione $g:Y\to X$ è l'inversa di $f$ se

$$
g\circ f=\operatorname{id}_X
\qquad\text{e}\qquad
f\circ g=\operatorname{id}_Y.
$$

Si scrive $g=f^{-1}$. Esiste se e solo se $f$ è biettiva.

## Intuizione

Se $f$ è un "tabellone" che manda ogni $x$ in un $y$, l'inversa legge lo stesso tabellone al contrario. Funziona solo se ogni $y$ compare una e una sola volta: la suriettività garantisce che $y$ abbia un'origine, l'iniettività che l'origine sia unica.

## Esempi

- $f(x)=2x+1$ da $\mathbb{R}$ in $\mathbb{R}$ ha inversa $f^{-1}(y)=\dfrac{y-1}{2}$.
- $x\mapsto x^2$ su tutto $\mathbb{R}$ non è invertibile, perché non è iniettiva.

## Come si dimostra

Si definisce $g(y)$ come l'unico $x$ tale che $f(x)=y$ e poi si verificano le due uguaglianze con le identità: vedi la [[2026-09-23 - Insiemi, applicazioni e spazi vettoriali#5.2 Costruzione dell’inversa di una biezione|costruzione dell'inversa]] nella lezione del 23 settembre.

## Vedi anche

- [[Funzione biettiva]]
- [[Composizione di funzioni]]
- [[Matrice invertibile]]
- [[Isomorfismo]]
