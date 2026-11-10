---
title: Immagine e controimmagine
type: voce
categoria: definizione
corsi:
- Analisi 1
- Geometria 1
introdotta_in: 2026-09-24 - Funzioni, composizione e principio d’induzione
alias:
- immagine
- controimmagine
- immagine di un insieme
- controimmagine di un insieme
sintesi: L'immagine di un sottoinsieme del dominio raccoglie i valori assunti dalla funzione, mentre la controimmagine di un sottoinsieme dell'arrivo raccoglie i punti che vi vengono mandati.
---
Data una funzione $f\colon A\to B$, l'**immagine** di un sottoinsieme del dominio è l'insieme dei valori che $f$ vi assume; la **controimmagine** di un sottoinsieme dell'arrivo è l'insieme dei punti del dominio che finiscono in esso.

## Definizione

Per $E\subseteq A$ e $D\subseteq B$:

$$
f(E)=\{f(a) : a\in E\},\qquad
f^{-1}(D)=\{a\in A : f(a)\in D\}.
$$

L'immagine di tutta la funzione è $f(A)$. La controimmagine è definita per *qualsiasi* funzione: la scrittura $f^{-1}(D)$ non richiede che $f$ sia invertibile.

## Intuizione

Graficamente, l'immagine si trova proiettando sull'asse $y$ la parte di grafico sopra $E$; la controimmagine si trova tagliando il grafico con le rette orizzontali che delimitano $D$ e proiettando sull'asse $x$. Per l'immagine non bastano gli estremi: bisogna tenere conto di massimi e minimi interni.

## Esempi

Per $f(x)=x^2$ su $\mathbb{R}$:

- $f([-1,2])=[0,4]$;
- $f^{-1}(\{4\})=\{-2,2\}$ e $f^{-1}(\{-1\})=\varnothing$.

Per $f(x)=|x^2-4|$ si ha $f([1,4])=[0,12]$ e $f^{-1}([-2,1])=[-\sqrt5,-\sqrt3]\cup[\sqrt3,\sqrt5]$.

## Vedi anche

- [[Funzione]]
- [[Funzione biettiva]]
- [[Funzione inversa]]
- [[Sottoinsieme]]
