---
title: Gruppo ciclico
type: voce
categoria: oggetto
corsi:
- Aritmetica
introdotta_in: 2026-10-28 - Gruppi ciclici, sottogruppi e permutazioni
alias:
- gruppi ciclici
- sottogruppo generato
- generatore
sintesi: Un gruppo in cui ogni elemento è una potenza di un unico elemento, detto generatore.
---

Un **gruppo ciclico** è un gruppo generato da un solo elemento: tutti gli altri si ottengono ripetendo l'operazione con lui (e con il suo inverso).

## Definizione

Dato un elemento $g$ di un [[Gruppo|gruppo]] $G$, il **sottogruppo generato** da $g$ è

$$
\langle g\rangle=\{g^n\mid n\in\mathbb Z\}
$$

(in notazione additiva $\{ng\mid n\in\mathbb Z\}$). Il gruppo $G$ è **ciclico** se $G=\langle g\rangle$ per qualche $g$, detto **generatore**.

Se $\operatorname{ord}(g)=m$ allora $\langle g\rangle=\{e,g,\dots,g^{m-1}\}$ ha $m$ elementi; altrimenti è infinito. A meno di [[Isomorfismo|isomorfismo]] i gruppi ciclici sono $\mathbb Z$ e $\mathbb Z/n\mathbb Z$.

## Intuizione

È come un orologio: continui a "fare un passo" e dopo $m$ passi torni al punto di partenza. Un gruppo ciclico è sempre abeliano, e ogni suo [[Sottogruppo|sottogruppo]] è ancora ciclico.

## Esempi

- $\mathbb Z=\langle1\rangle=\langle-1\rangle$.
- In $\mathbb Z/12\mathbb Z$ si ha $\langle\overline3\rangle=\{\overline0,\overline3,\overline6,\overline9\}$.
- Le radici $n$-esime dell'unità formano il gruppo ciclico $\{1,\zeta,\dots,\zeta^{n-1}\}$ con $\zeta=e^{2\pi i/n}$.

## Come si dimostra

$\langle g\rangle$ è un sottogruppo grazie al criterio: $g^r(g^s)^{-1}=g^{r-s}$. La dimostrazione è nella sezione [[2026-10-28 - Gruppi ciclici, sottogruppi e permutazioni#4. Gruppi ciclici|sui gruppi ciclici]] della lezione del 28 ottobre.

## Vedi anche

- [[Ordine di un elemento]]
- [[Sottogruppo]]
- [[Radice n-esima dell'unità]]
- [[Isomorfismo]]
