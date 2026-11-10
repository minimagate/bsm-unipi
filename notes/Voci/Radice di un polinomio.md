---
title: Radice di un polinomio
type: voce
categoria: definizione
corsi:
- Geometria 1
introdotta_in: 2026-10-01 - Fattorizzazione dei polinomi e radici complesse
alias:
- radici di un polinomio
- molteplicità
- molteplicità di una radice
sintesi: Una radice di un polinomio è un valore in cui il polinomio si annulla; la molteplicità indica quante volte compare il fattore corrispondente.
---

Una **radice** di un [[Polinomio|polinomio]] $P$ è un elemento $z_0$ per cui $P(z_0)=0$. La **molteplicità** di una radice dice quante volte il fattore $z-z_0$ compare nella fattorizzazione.

## Definizione

Dato $P$, si dice che $z_0$ è una radice di molteplicità $k$ se

$$
P(z)=(z-z_0)^kQ(z)\qquad\text{con }Q(z_0)\neq 0.
$$

Equivalentemente, $k$ è il massimo esponente per cui $(z-z_0)^k\mid P(z)$. Per il teorema del fattore, $P(z_0)=0$ se e solo se $z-z_0$ divide $P(z)$.

## Intuizione

Trovata una radice, si può dividere per $z-z_0$ e si abbassa il grado di uno; se il quoziente ha ancora la stessa radice, si divide di nuovo. Un polinomio non nullo di grado $n$ ha al più $n$ radici contate con molteplicità, e sui complessi ne ha esattamente $n$ per il [[Teorema fondamentale dell'algebra]].

## Esempi

- $P(z)=(z-1)^5$ ha l'unica radice $1$, di molteplicità $5$.
- $P(z)=(z-1)^2(z-3)^4(z-5)^3$ ha grado $9$ e radici $1,3,5$ di molteplicità $2,4,3$.
- Per un polinomio a coefficienti reali, le radici non reali vengono a coppie coniugate, con la stessa molteplicità (vedi [[Coniugio complesso]]).

## Come si dimostra

Il teorema del fattore segue dalla divisione di $P$ per $z-z_1$: il resto è una costante, e vale $P(z_1)$. Vedi [[2026-10-01 - Fattorizzazione dei polinomi e radici complesse#4. Molteplicità delle radici|le molteplicità]] e [[2026-10-01 - Fattorizzazione dei polinomi e radici complesse#2. Corollario: fattorizzazione completa in fattori lineari|la fattorizzazione completa]].

## Vedi anche

- [[Polinomio]]
- [[Teorema fondamentale dell'algebra]]
- [[Radice n-esima dell'unità]]
- [[Divisibilità]]
