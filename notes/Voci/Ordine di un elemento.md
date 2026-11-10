---
title: Ordine di un elemento
type: voce
categoria: definizione
corsi:
- Aritmetica
introdotta_in: 2026-11-01 - Gruppi ciclici, ordini e sottogruppi modulari
alias:
- ordine
- ordine di un gruppo
sintesi: Il più piccolo esponente positivo che porta un elemento del gruppo nell'elemento neutro.
---

L'**ordine** di un elemento è il numero di passi dopo i quali le sue potenze tornano all'elemento neutro. L'**ordine di un gruppo** è invece il numero dei suoi elementi.

## Definizione

Sia $g$ un elemento di un [[Gruppo|gruppo]] $G$ con neutro $e$. L'ordine di $g$ è

$$
\operatorname{ord}(g)=\min\{k>0\mid g^k=e\},
$$

e vale $+\infty$ se non esiste alcun $k>0$ con $g^k=e$. (In notazione additiva: il minimo $m>0$ con $mg=0$.)

Valgono: $\operatorname{ord}(g)=|\langle g\rangle|$; se $g^m=e$ allora $\operatorname{ord}(g)\mid m$; in un gruppo finito $\operatorname{ord}(g)\mid|G|$; se $\operatorname{ord}(g)=n$ allora $\operatorname{ord}(g^k)=\dfrac{n}{\gcd(n,k)}$.

## Intuizione

Se $g$ ha ordine $m$, le potenze di $g$ si ripetono con periodo $m$, come le ore su un orologio: $g^{k+m}=g^k$. Perciò gli esponenti si contano modulo $m$.

## Esempi

- In $\mathbb Z/12\mathbb Z$ (additivo), $\overline3$ ha ordine $4$ perché $4\cdot\overline3=\overline0$.
- Se $\operatorname{ord}(g)=6$: $\operatorname{ord}(g^2)=3$, $\operatorname{ord}(g^3)=2$, $\operatorname{ord}(g^5)=6$.
- Modulo $13$, $3^3=27\equiv1$, quindi $3$ ha ordine $3$ in $(\mathbb Z/13\mathbb Z)^\times$.

## Come si dimostra

La formula per $\operatorname{ord}(g^k)$ si ottiene da $g^{km}=e\iff n\mid km$ e dal [[Lemma di Euclide|lemma di Euclide]]; si veda la sezione [[2026-11-01 - Gruppi ciclici, ordini e sottogruppi modulari#6. Ordine di una potenza|sull'ordine di una potenza]] della lezione del 1 novembre.

## Vedi anche

- [[Gruppo ciclico]]
- [[Teorema di Lagrange]]
- [[Elementi invertibili modulo n]]
- [[Prodotto diretto]]
