---
title: Algoritmo di Euclide
type: voce
categoria: metodo
corsi:
- Aritmetica
- Fondamenti di Programmazione
introdotta_in: 2026-09-19 - Pensiero computazionale, algoritmi e modelli di calcolo
alias:
- algoritmo euclideo
sintesi: Procedimento che calcola il massimo comun divisore di due interi sostituendo ripetutamente il problema con uno più piccolo.
---

L'**algoritmo di Euclide** è un procedimento per calcolare il [[Massimo comun divisore|massimo comun divisore]] di due numeri senza elencare i loro divisori. Nel corso lo si incontra come primo esempio di algoritmo "intelligente".

## Enunciato

Per interi positivi $x$ e $y$ valgono:

$$
\begin{aligned}
\operatorname{MCD}(x,x) &= x, \\
\operatorname{MCD}(x,y) &= \operatorname{MCD}(x-y,y) && \text{se } x>y, \\
\operatorname{MCD}(x,y) &= \operatorname{MCD}(x,y-x) && \text{se } x<y.
\end{aligned}
$$

Applicando più volte la seconda o la terza regola, il problema si riduce a uno sempre più semplice, fino al caso $x=y$.

## Intuizione

Ogni divisore comune di $x$ e $y$ divide anche la loro differenza, e viceversa. Quindi sottrarre il più piccolo dal più grande non cambia l'MCD, ma rimpicciolisce i numeri. Nella versione per divisioni, che si studia in Aritmetica, la sottrazione ripetuta è sostituita dal resto della [[Divisione euclidea|divisione euclidea]].

## Esempi

$\operatorname{MCD}(12,8)=\operatorname{MCD}(4,8)=\operatorname{MCD}(4,4)=4$.

Con numeri più grandi: $\operatorname{MCD}(21,15)=\operatorname{MCD}(6,15)=\operatorname{MCD}(6,9)=\operatorname{MCD}(6,3)=\operatorname{MCD}(3,3)=3$.

## Vedi anche

- [[Massimo comun divisore]]
- [[Divisione euclidea]]
- [[Algoritmo]]
- [[Identità di Bézout]]
