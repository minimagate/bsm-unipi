---
title: Funzione biettiva
type: voce
categoria: definizione
corsi:
- Analisi 1
- Aritmetica
- Geometria 1
introdotta_in: 2026-09-23 - Insiemi, applicazioni e spazi vettoriali
alias:
- funzione iniettiva
- funzione suriettiva
- iniettività
- suriettività
- biettività
- biiettività
- biezione
- biiezione
- applicazione iniettiva
- applicazione suriettiva
- applicazione biettiva
sintesi: Una funzione è iniettiva se non manda due elementi distinti nello stesso punto, suriettiva se raggiunge ogni elemento del codominio, biettiva se è entrambe le cose.
---

Una [[Funzione|funzione]] $f:X\to Y$ è **iniettiva** se elementi distinti hanno immagini distinte, **suriettiva** se ogni elemento di $Y$ è raggiunto, **biettiva** se è entrambe le cose. Le funzioni biettive si dicono anche corrispondenze biunivoche.

## Definizione

- **Iniettiva**: $x\neq x'\Rightarrow f(x)\neq f(x')$, o equivalentemente $f(x)=f(x')\Rightarrow x=x'$.
- **Suriettiva**: $\forall y\in Y\ \exists x\in X$ tale che $f(x)=y$, cioè $f(X)=Y$.
- **Biettiva**: iniettiva e suriettiva; ogni $y\in Y$ è immagine di uno e un solo $x\in X$.

## Intuizione

L'iniettività dice che nessun elemento di $Y$ viene "colpito due volte"; la suriettività che nessun elemento di $Y$ viene "dimenticato". Una biezione accoppia perfettamente gli elementi di $X$ con quelli di $Y$, ed è proprio ciò che serve per poter tornare indietro con la [[Funzione inversa]].

## Esempi

- $f:\mathbb{R}\to\mathbb{R}$, $f(x)=x^2$ non è iniettiva ($f(1)=f(-1)$) né suriettiva ($-1$ non è raggiunto).
- $g:\mathbb{R}\to\mathbb{R}$, $g(x)=2x+1$ è biettiva.
- Restringendo il codominio, $x\mapsto x^2$ da $\mathbb{R}$ a $[0,+\infty)$ diventa suriettiva.

## Come si dimostra

Per l'iniettività si assume $f(x)=f(x')$ e si ricava $x=x'$; per la suriettività si fissa $y$ e si cerca un $x$ con $f(x)=y$. Il legame con l'inversa è nella [[2026-09-23 - Insiemi, applicazioni e spazi vettoriali#5.2 Costruzione dell’inversa di una biezione|costruzione dell'inversa di una biezione]].

## Vedi anche

- [[Funzione]]
- [[Funzione inversa]]
- [[Composizione di funzioni]]
- [[Isomorfismo]]
