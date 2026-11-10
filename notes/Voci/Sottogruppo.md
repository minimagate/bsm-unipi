---
title: Sottogruppo
type: voce
categoria: definizione
corsi:
- Aritmetica
introdotta_in: 2026-10-28 - Gruppi ciclici, sottogruppi e permutazioni
alias:
- sottogruppi
- criterio del sottogruppo
sintesi: Un sottoinsieme di un gruppo che con la stessa operazione è a sua volta un gruppo.
---

Un **sottogruppo** è un pezzo di un gruppo che è chiuso rispetto all'operazione e agli inversi, e quindi è un gruppo a sé.

## Definizione

Sia $G$ un [[Gruppo|gruppo]]. Un sottoinsieme $H\subseteq G$ è un sottogruppo, e si scrive $H\leq G$, se con l'operazione di $G$ è a sua volta un gruppo. Il neutro e gli inversi di $H$ sono quelli di $G$.

**Criterio del sottogruppo.** $H\leq G$ se e solo se $H\neq\varnothing$ e per ogni $x,y\in H$ vale $xy^{-1}\in H$.

## Intuizione

Per controllare che $H$ sia un sottogruppo non serve ripetere tutti gli assiomi: l'associatività è ereditata, e il criterio racchiude in una sola condizione la chiusura per prodotto e inverso. Banalmente $G$ e $\{e\}$ sono sempre sottogruppi.

## Esempi

- $n\mathbb Z\leq\mathbb Z$: se $x=na$ e $y=nb$ allora $x-y=n(a-b)\in n\mathbb Z$.
- Per $d,m\in\mathbb Z$: $d\mathbb Z\subseteq m\mathbb Z\iff m\mid d$, e $d\mathbb Z\cap m\mathbb Z=\operatorname{mcm}(d,m)\,\mathbb Z$.
- L'intersezione di due sottogruppi è un sottogruppo; l'unione lo è solo se uno è contenuto nell'altro.

## Come si dimostra

Dal criterio si ricava $e=aa^{-1}\in H$, poi $x^{-1}=ex^{-1}\in H$, poi $xy=x(y^{-1})^{-1}\in H$. Si veda la sezione [[2026-10-28 - Gruppi ciclici, sottogruppi e permutazioni#3.2 Criterio del sottogruppo|sul criterio del sottogruppo]] della lezione del 28 ottobre.

## Vedi anche

- [[Gruppo ciclico]]
- [[Centro di un gruppo]]
- [[Classe laterale]]
- [[Sottogruppo normale]]
