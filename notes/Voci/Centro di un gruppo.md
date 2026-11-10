---
title: Centro di un gruppo
type: voce
categoria: oggetto
corsi:
- Aritmetica
introdotta_in: 2026-10-28 - Gruppi ciclici, sottogruppi e permutazioni
alias:
- centro
sintesi: L'insieme degli elementi di un gruppo che commutano con tutti gli altri.
---

Il **centro** di un gruppo è l'insieme degli elementi che "vanno d'accordo" con tutti: commutano con ogni elemento del gruppo.

## Definizione

Per un [[Gruppo|gruppo]] $G$,

$$
Z(G)=\{z\in G\mid zg=gz\ \text{per ogni }g\in G\}.
$$

Il centro è un [[Sottogruppo|sottogruppo]] di $G$ (contiene $e$ ed è chiuso per prodotto e inverso) ed è anche un [[Sottogruppo normale|sottogruppo normale]]. Un gruppo è abeliano se e solo se $Z(G)=G$. Nel [[Prodotto diretto|prodotto diretto]] vale $Z(G_1\times G_2)=Z(G_1)\times Z(G_2)$.

## Intuizione

Misura "quanto è commutativo" il gruppo: più grande è il centro, più il gruppo somiglia a un gruppo abeliano.

## Esempi

- In $(\mathbb Z/12\mathbb Z,+)$ il centro è tutto il gruppo.
- In $S_3$ il centro è $\{\operatorname{id}\}$: per esempio $(1\ 2\ 3)$ non commuta con $(1\ 2)$.

## Come si dimostra

Se $x,y\in Z(G)$ e $g\in G$ allora $(xy)g=x(gy)=(xg)y=g(xy)$, quindi $xy\in Z(G)$; i dettagli sono nella [[2026-10-28 - Gruppi ciclici, sottogruppi e permutazioni#5. Il centro di un gruppo|sezione sul centro]] della lezione del 28 ottobre.

## Vedi anche

- [[Sottogruppo]]
- [[Sottogruppo normale]]
- [[Gruppo delle permutazioni]]
- [[Prodotto diretto]]
