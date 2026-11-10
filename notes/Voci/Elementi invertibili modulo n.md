---
title: Elementi invertibili modulo n
type: voce
categoria: definizione
corsi:
- Aritmetica
introdotta_in: 2026-10-21 - Relazioni di equivalenza e strutture quoziente
alias:
- gruppo delle unità
- invertibili modulo n
- unità modulo n
sintesi: Le classi modulo n che hanno inverso moltiplicativo sono esattamente quelle il cui rappresentante è coprimo con n.
---

Una classe $[a]_n$ è **invertibile** in $\mathbb Z/n\mathbb Z$ se esiste una classe $[x]_n$ con $[a]_n[x]_n=[1]_n$. Le classi invertibili, con il prodotto, formano un gruppo, indicato con $(\mathbb Z/n\mathbb Z)^\times$.

## Enunciato

**Teorema.** La classe $[a]_n$ è invertibile in $\mathbb Z/n\mathbb Z$ se e solo se

$$
\gcd(a,n)=1.
$$

In tal caso l'inverso è la classe di un intero $x$ con $ax\equiv1\pmod n$ (vedi [[Inverso modulo n]]). La proprietà dipende solo dalla classe: rappresentanti diversi hanno lo stesso MCD con $n$.

## Intuizione

Dividere per $a$ modulo $n$ è possibile solo se $a$ non "condivide fattori" con $n$. Se $p$ è primo ogni classe non nulla è invertibile e $\mathbb Z/p\mathbb Z$ è un [[Campo|campo]].

## Esempi

- Modulo $12$ le classi invertibili sono $[1],[5],[7],[11]$, e ciascuna è inversa di se stessa: $5\cdot5=25\equiv1$, $7\cdot7=49\equiv1$, $11\cdot11=121\equiv1\pmod{12}$.
- $[2]_{12}$ non è invertibile, perché $\gcd(2,12)=2$.

## Come si dimostra

Se $ax-kn=1$ ogni divisore comune di $a$ e $n$ divide $1$; viceversa, se $\gcd(a,n)=1$, l'[[Identità di Bézout|identità di Bézout]] dà $ax+nk=1$, cioè $ax\equiv1$. La dimostrazione è nella [[2026-10-21 - Relazioni di equivalenza e strutture quoziente|lezione del 21 ottobre]].

## Vedi anche

- [[Inverso modulo n]]
- [[Massimo comun divisore]]
- [[Identità di Bézout]]
- [[Congruenza modulo n]]
