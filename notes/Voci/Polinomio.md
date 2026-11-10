---
title: Polinomio
type: voce
categoria: oggetto
corsi:
- Geometria 1
introdotta_in: 2026-09-30 - Spazi vettoriali, esempi e sottospazi
alias:
- polinomi
- anello dei polinomi
sintesi: Un polinomio a coefficienti in un campo è un'espressione formale a0 più a1 x più fino a an x alla n, e i polinomi formano uno spazio vettoriale.
---

Un **polinomio** nella variabile $x$ a coefficienti in un campo $K$ è un'espressione formale fatta di potenze di $x$ con coefficienti in $K$. L'insieme di tutti i polinomi si indica con $K[x]$.

## Definizione

$$
p(x)=a_0+a_1x+a_2x^2+\cdots+a_nx^n,
\qquad a_i\in K.
$$

La $x$ è un simbolo formale, non necessariamente una variabile di funzione. Il **grado** di un polinomio non nullo è $\deg p=\max\{k\mid a_k\neq 0\}$. La somma si fa coefficiente per coefficiente, il prodotto per uno scalare $\alpha\in K$ moltiplica tutti i coefficienti.

Valgono $\deg(p+q)\leq\max\{\deg p,\deg q\}$ e, per il polinomio nullo, nessun grado.

## Intuizione

Per l'algebra lineare conta soprattutto che $K[x]$, con somma e prodotto per scalare, è uno [[Spazio vettoriale|spazio vettoriale]] su $K$: i monomi $1,x,x^2,\dots$ ne sono una [[Base di uno spazio vettoriale|base]] (infinita). I polinomi di grado esattamente $n$ non formano uno spazio vettoriale (la somma può abbassare il grado), quelli di grado al più $n$ sì: è lo spazio $K_n[x]$.

## Esempi

- $p(x)=3x^5-2x^2+1$ ha grado $5$.
- Se $p=3x^5+2x^3$ e $q=-3x^5+5x^3$, la somma è $7x^3$, di grado $3<5$.
- Sui complessi ogni polinomio non costante ha una radice: vedi il [[Teorema fondamentale dell'algebra]].

## Come si dimostra

Che $K[x]$ sia uno spazio vettoriale si verifica coefficiente per coefficiente, riducendosi agli assiomi di $K$: vedi [[2026-09-30 - Spazi vettoriali, esempi e sottospazi#7. Polinomi a coefficienti in un campo|i polinomi a coefficienti in un campo]].

## Vedi anche

- [[Radice di un polinomio]]
- [[Spazio vettoriale]]
- [[Campo]]
- [[Teorema fondamentale dell'algebra]]
