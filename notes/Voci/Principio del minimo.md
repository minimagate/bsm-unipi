---
title: Principio del minimo
type: voce
categoria: teorema
corsi:
- Aritmetica
introdotta_in: 2026-09-23 - Numeri naturali, induzione e fattorizzazione
alias:
- buon ordinamento
sintesi: Ogni sottoinsieme non vuoto dei numeri naturali possiede un elemento minimo.
---

Il **principio del minimo**, detto anche principio del buon ordinamento, afferma che ogni sottoinsieme non vuoto di $\mathbb{N}$ ha un elemento più piccolo di tutti gli altri.

## Enunciato

Se $S\subseteq\mathbb{N}$ e $S\neq\varnothing$, allora esiste $m\in S$ tale che

$$m\le n\qquad\forall n\in S.$$

L'elemento $m$ è il minimo di $S$. Il principio è equivalente al [[Principio di induzione]].

## Intuizione

Colora alcuni punti sulla retta dei naturali $0,1,2,3,\ldots$ e cammina da sinistra verso destra: prima o poi incontri un punto colorato, e il primo che incontri è il minimo. Non si può "scendere all'infinito", perché a sinistra c'è il punto di partenza $0$. Per questo non vale sugli interi o sui reali positivi.

## Esempi

- Se $S=\{n\in\mathbb{N}: n^2>50\}$, il minimo è $8$, perché $7^2=49$ non basta e $8^2=64$.
- Nella [[Divisione euclidea]] il resto è il minimo dell'insieme $\{a-qb\ge 0\}$.

## Come si dimostra

Il principio del minimo e l'induzione si dimostrano a vicenda: si usa il minimo controesempio per dedurre l'induzione, e l'induzione sulla proprietà "$n\notin S$" per dedurre il minimo. Vedi [[2026-09-23 - Numeri naturali, induzione e fattorizzazione#6. Dimostrazione del principio di induzione mediante il principio del minimo|la dimostrazione in lezione]].

## Vedi anche

- [[Numero naturale]]
- [[Principio di induzione]]
- [[Induzione forte]]
- [[Divisione euclidea]]
