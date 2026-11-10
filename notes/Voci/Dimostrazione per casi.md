---
title: Dimostrazione per casi
type: voce
categoria: metodo
corsi:
- Fondamenti di Programmazione
introdotta_in: 2026-09-23 - Forme normali, tecniche di dimostrazione e logica del primo ordine
alias:
- per casi
sintesi: Per dimostrare una tesi si sceglie una proposizione e si dimostra la tesi sia nel caso in cui sia vera sia nel caso in cui sia falsa.
---

La **dimostrazione per casi** spezza una dimostrazione in due (o più) situazioni che esauriscono tutte le possibilità.

## Enunciato

$$
(P\Rightarrow Q)\land(\neg P\Rightarrow Q)\equiv Q.
$$

Per dimostrare $Q$ si sceglie una proposizione $P$ conveniente e si dimostra $Q$ sotto l'ipotesi $P$ e sotto l'ipotesi $\neg P$.

## Intuizione

Per il terzo escluso, $P$ è vera oppure falsa: se la tesi regge in entrambi i casi, regge sempre. Funziona bene quando in ciascun caso si guadagna un'ipotesi in più con cui lavorare. La scelta di $P$ è la parte creativa: va fatta in modo che, sotto $P$ e sotto $\neg P$, la dimostrazione diventi più semplice. Si può usare anche con più di due casi, purché i casi coprano tutte le possibilità.

## Esempi

- Per dimostrare che $n(n+1)$ è pari si distinguono i casi "$n$ pari" e "$n$ dispari": in entrambi uno dei due fattori è pari.
- Nel calcolo proposizionale, la legge $(P\Rightarrow Q)\land(\neg P\Rightarrow Q)\equiv Q$ si verifica con una [[Tavola di verità|tavola di verità]] su due simboli.

## Vedi anche

- [[Dimostrazione per assurdo]]
- [[Contrapposizione]]
- [[Implicazione]]
