---
title: Formula di Legendre
type: voce
categoria: teorema
corsi:
- Aritmetica
introdotta_in: 2026-10-14 - Sviluppi decimali razionali e fattorizzazione dei denominatori
alias:
- esponente di un primo nel fattoriale
sintesi: L'esponente di un primo nella fattorizzazione di n fattoriale è la somma delle parti intere di n diviso le potenze del primo.
---

La **formula di Legendre** calcola quante volte un primo $p$ compare nella fattorizzazione di $n!$.

## Enunciato

Indicando con $v_p(N)$ l'esponente di $p$ in $N$,

$$v_p(n!)=\sum_{k\ge1}\left\lfloor\frac{n}{p^k}\right\rfloor.$$

La somma è finita: per $p^k>n$ i termini sono nulli.

## Intuizione

I multipli di $p$ tra $1$ e $n$ sono $\lfloor n/p\rfloor$, ciascuno porta almeno un fattore $p$; i multipli di $p^2$ ne portano uno in più, e così via. Sommando i multipli di ogni potenza si contano tutti i fattori $p$.

Si ottiene anche una dimostrazione "per colonne": gli interi divisibili esattamente per $p^k$ sono $\lfloor n/p^k\rfloor-\lfloor n/p^{k+1}\rfloor$ e ciascuno porta $k$ fattori $p$; la somma telescopica restituisce la stessa formula.

## Esempi

- $v_2(19!)=9+4+2+1=16$.
- $v_5(100!)=20+4=24$, quindi $100!$ finisce con $24$ zeri.

## Come si dimostra

Due dimostrazioni, per righe e per colonne (con somma telescopica), nella [[2026-10-14 - Sviluppi decimali razionali e fattorizzazione dei denominatori#10. Formula generale di Legendre|lezione del 14 ottobre]].

## Vedi anche

- [[Numero primo]]
- [[Teorema fondamentale dell'aritmetica]]
- [[Coefficiente binomiale]]
- [[Sviluppo decimale]]
