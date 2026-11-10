---
title: Gruppo
type: voce
categoria: oggetto
corsi:
- Aritmetica
- Geometria 1
introdotta_in: 2026-10-21 - Relazioni di equivalenza e strutture quoziente
alias:
- gruppi
- struttura di gruppo
- gruppo abeliano
sintesi: Un insieme con un'operazione associativa dotata di elemento neutro e in cui ogni elemento ha un inverso.
---

Un **gruppo** è un insieme con una sola operazione che si comporta bene: si può combinare, annullare e non servono parentesi. Se l'operazione è anche commutativa il gruppo si dice **abeliano**.

## Definizione

Un insieme $G$ con un'operazione $\star$ è un gruppo se:

1. $\star$ è interna: $x\star y\in G$ per ogni $x,y\in G$;
2. è associativa: $(x\star y)\star z=x\star(y\star z)$;
3. esiste un elemento neutro $e$ con $x\star e=e\star x=x$;
4. ogni $x$ ha un inverso $x^{-1}$ con $x\star x^{-1}=x^{-1}\star x=e$.

Se vale anche $x\star y=y\star x$, il gruppo è abeliano. In notazione additiva si scrivono $x+y$, $0$ e $-x$.

## Intuizione

Il gruppo astrae le simmetrie e le "operazioni reversibili": ogni mossa si può disfare. Dimostrare un fatto una volta nei gruppi significa averlo dimostrato per tutti gli esempi, dagli interi con la somma alle permutazioni.

## Esempi

- $(\mathbb Z,+)$ e $(\mathbb Z/n\mathbb Z,+)$ sono gruppi abeliani.
- $(\mathbb Z,\cdot)$ **non** è un gruppo: per esempio $2$ non ha inverso, perché $2x=1$ non ha soluzioni intere.
- Le [[Gruppo delle permutazioni|permutazioni]] di un insieme formano un gruppo, non abeliano se l'insieme ha almeno $3$ elementi.

## Come si dimostra

Le proprietà elementari (unicità di neutro e inverso, $(gh)^{-1}=h^{-1}g^{-1}$, cancellazione) sono dimostrate nella [[2026-10-28 - Gruppi ciclici, sottogruppi e permutazioni#1. Esempi di gruppi|lezione del 28 ottobre]].

## Vedi anche

- [[Sottogruppo]]
- [[Anello]]
- [[Omomorfismo]]
- [[Gruppo ciclico]]
