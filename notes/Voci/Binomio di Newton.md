---
title: Binomio di Newton
type: voce
categoria: teorema
corsi:
- Aritmetica
introdotta_in: 2026-09-30 - Successioni ricorrenti e formule combinatorie
alias:
- formula del binomio
- formula del binomio di Newton
sintesi: Lo sviluppo della potenza di una somma di due termini si scrive con i coefficienti binomiali.
---

Il **binomio di Newton** è la formula per sviluppare la potenza $n$-esima di una somma di due termini.

## Enunciato

Per ogni $n\in\mathbb{N}$,

$$(a+b)^n=\sum_{k=0}^{n}\binom{n}{k}a^kb^{n-k}.$$

Con $a=b=1$ si ottiene $\sum_k\binom{n}{k}=2^n$; con $a=1,\ b=-1$ (e $n>0$) si ottiene $\sum_k(-1)^k\binom{n}{k}=0$.

## Intuizione

Sviluppando $(a+b)(a+b)\cdots(a+b)$ da ogni parentesi scegli $a$ oppure $b$. Per ottenere $a^kb^{n-k}$ devi scegliere $a$ in esattamente $k$ parentesi, e puoi farlo in $\binom{n}{k}$ modi: ecco il coefficiente.

I coefficienti $\binom{n}{k}$ formano le righe del triangolo di Pascal. Per questo la formula è anche un ponte tra algebra e conteggio: ogni identità sui binomiali ha una lettura combinatoria, e viceversa.

## Esempi

- $(a+b)^2=a^2+2ab+b^2$ perché $\binom20,\binom21,\binom22=1,2,1$.
- $(a+b)^3=a^3+3a^2b+3ab^2+b^3$.
- Con $a=1,b=-1$: i sottoinsiemi di cardinalità pari e dispari sono $2^{n-1}$ ciascuno.

## Come si dimostra

Si dimostra per induzione su $n$, moltiplicando per $a+b$ e usando l'identità di Pascal $\binom{n}{j-1}+\binom{n}{j}=\binom{n+1}{j}$. Vedi [[2026-09-30 - Successioni ricorrenti e formule combinatorie#6.4 Dimostrazione per induzione|la lezione del 30 settembre]].

## Vedi anche

- [[Coefficiente binomiale]]
- [[Principio di induzione]]
- [[Insieme delle parti]]
- [[Principio di inclusione-esclusione]]
