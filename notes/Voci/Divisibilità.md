---
title: Divisibilità
type: voce
categoria: definizione
corsi:
- Aritmetica
introdotta_in: 2026-10-05 - Divisione euclidea, massimo comun divisore e identità di Bézout
alias:
- divisore
- multiplo
- divide
sintesi: Un intero a divide un intero b se b è un multiplo intero di a.
---

La **divisibilità** è la relazione tra interi per cui $a$ *divide* $b$ quando $b$ è un multiplo di $a$.

## Definizione

Per $a,b\in\mathbb{Z}$ si scrive $a\mid b$ se esiste $k\in\mathbb{Z}$ tale che

$$b=ka.$$

Allora $a$ è un *divisore* di $b$ e $b$ è un *multiplo* di $a$. La relazione è riflessiva ($a\mid a$) e transitiva ($a\mid b,\ b\mid c\Rightarrow a\mid c$); non è simmetrica, e su $\mathbb{N}$ è antisimmetrica, quindi è un ordine parziale (non totale: $2$ e $3$ non sono confrontabili).

## Intuizione

Occhio al verso: $a\mid b$ si legge "$a$ sta dentro $b$". Per esempio $2\mid6$ ma $6\nmid2$. Se $d$ divide $a$ e $b$, divide anche ogni combinazione $ax+by$ a coefficienti interi: è un fatto usato continuamente.

## Esempi

- $2\mid6$ perché $6=3\cdot2$.
- $3\nmid10$: nessun intero $k$ soddisfa $10=3k$.
- Un [[Numero primo]] ha come soli divisori positivi $1$ e se stesso.

## Come si dimostra

La transitività: se $b=k_1a$ e $c=k_2b$, allora $c=(k_1k_2)a$. Vedi [[2026-10-05 - Divisione euclidea, massimo comun divisore e identità di Bézout#5. Divisibilità|la lezione del 5 ottobre]].

## Vedi anche

- [[Divisione euclidea]]
- [[Massimo comun divisore]]
- [[Numero primo]]
- [[Congruenza modulo n]]
