---
title: Teorema di deduzione
type: voce
categoria: teorema
corsi:
- Fondamenti di Programmazione
introdotta_in: 2026-10-12 - Semantica della logica del primo ordine
alias:
- deduzione
sintesi: Per dimostrare un'implicazione basta assumere l'antecedente come ipotesi e dimostrare il conseguente.
---

Il **teorema di deduzione** giustifica la tecnica che si usa continuamente: per dimostrare $P\Rightarrow Q$ si assume $P$ e si dimostra $Q$.

## Enunciato

$$
\Gamma\vdash P\Rightarrow Q
\quad\text{se e solo se}\quad
\Gamma,P\vdash Q.
$$

Cioè $P\Rightarrow Q$ è dimostrabile dalle premesse $\Gamma$ se e solo se $Q$ è dimostrabile da $\Gamma$ con l'aggiunta dell'ipotesi $P$.

## Intuizione

Nel [[Calcolo proposizionale|calcolo proposizionale]] si faceva già: "supponiamo $P$ e mostriamo $Q$". Il teorema dice che farlo è lecito. Lavorando così si possono usare sia le leggi generali (formule valide) sia $P$ come ipotesi; ciò che si ottiene è che $Q$ è [[Conseguenza logica|conseguenza logica]] di $P$ e delle altre ipotesi.

## Esempi

Per mostrare $(\forall x.\,p(x))\Rightarrow(\exists x.\,p(x))$ si assume $\forall x.\,p(x)$. Per eliminazione dell'universale si ottiene $p(a)$ per un termine $a$, e per introduzione dell'esistenziale da $p(a)$ si ottiene $\exists x.\,p(x)$.

Nel CP: sotto l'ipotesi $P$ si ha $P\land Q\equiv\mathrm T\land Q\equiv Q$, e quindi $P\Rightarrow(P\land Q\equiv Q)$.

## Vedi anche

- [[Regola di inferenza]]
- [[Implicazione]]
- [[Conseguenza logica]]
- [[Skolemizzazione]]
