---
title: Minimo comune multiplo
type: voce
categoria: definizione
corsi:
- Aritmetica
introdotta_in: 2026-10-13 - Divisori, algoritmo di Euclide e conteggio combinatorio
alias:
- mcm
- lcm
sintesi: Il minimo comune multiplo di due interi è il più piccolo intero positivo multiplo di entrambi.
---

Il **minimo comune multiplo** (mcm, in inglese $\operatorname{lcm}$) di due interi positivi è il più piccolo multiplo positivo comune a entrambi.

## Definizione

Con le fattorizzazioni $A=\prod p_i^{\alpha_i}$ e $B=\prod p_i^{\beta_i}$:

$$\operatorname{lcm}(A,B)=\prod p_i^{\max(\alpha_i,\beta_i)},\qquad \gcd(A,B)=\prod p_i^{\min(\alpha_i,\beta_i)}.$$

Poiché $\min+\max=\alpha_i+\beta_i$, vale

$$\gcd(A,B)\operatorname{lcm}(A,B)=AB.$$

## Intuizione

Un multiplo comune deve contenere ogni primo con esponente almeno pari a entrambi, e il minimo possibile è il massimo dei due. Passando dal [[Massimo comun divisore]] al mcm si scambiano minimi e massimi.

Dalla relazione $\operatorname{lcm}(A,B)=\frac{AB}{\gcd(A,B)}$ si calcola il mcm senza fattorizzare, una volta noto il MCD tramite l'algoritmo di Euclide. Il mcm serve, per esempio, per sommare frazioni e per sistemi di congruenze con moduli non coprimi.

## Esempi

$12=2^2\cdot3$ e $18=2\cdot3^2$: $\gcd=6$, $\operatorname{lcm}=36$, e $6\cdot36=216=12\cdot18$. Per moduli coprimi $\operatorname{lcm}(m_1,m_2)=m_1m_2$.

## Come si dimostra

Vedi [[2026-10-13 - Divisori, algoritmo di Euclide e conteggio combinatorio#Minimo comune multiplo|la lezione del 13 ottobre]].

## Vedi anche

- [[Massimo comun divisore]]
- [[Teorema fondamentale dell'aritmetica]]
- [[Teorema cinese del resto]]
- [[Numeri coprimi]]
